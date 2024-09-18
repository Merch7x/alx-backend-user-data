#!/usr/bin/env python3
"""New View for Session Authentication"""
from api.v1.views import app_views
from models.user import User
from flask import request, abort, jsonify


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Logs a User in"""
    email = request.form.get("email")
    passwd = request.form.get("password")

    if not email or email is None:
        return jsonify({"error": "email missing"}), 400

    if not passwd or passwd is None:
        return jsonify({"error": "password missing"}), 400

    user = User.search({"email": email})
    if not user or user is None:
        return jsonify({"error": "no user found for this email"}), 404

    if not user[0].is_valid_password(passwd):
        return jsonify({"error": "wrong password"}), 401

    from api.v1.app import auth
    auth.create_session(user[0].id)

    authed_user = jsonify(user[0].to_json())
    return authed_user


@app_views.route('/auth_session/logout', methods=['DELETE'], strict_slashes=False)
def logout():
    """Logout a user by deleting saved session"""
    from api.v1.app import auth
    destroy_sesh = auth.destroy_session(request)
    if destroy_sesh is False:
        abort(404)
    return {}, 200
