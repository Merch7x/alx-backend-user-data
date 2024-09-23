#!/usr/bin/env python3
"""A flask application"""
from flask import Flask, jsonify, request, abort, make_response, \
    redirect
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def index():
    """Index route"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=["POST"], strict_slashes=False)
def users():
    """Register a user"""
    email = request.form.get("email")
    password = request.form.get("password")

    try:
        AUTH.register_user(email, password)
        return jsonify(
            {"email": f"{email}", "message": "user created"}), 201
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=["POST"], strict_slashes=False)
def login():
    """Log a user in"""
    email = request.form.get("email")
    password = request.form.get("password")

    if AUTH.valid_login(email, password):
        session_id = AUTH.create_session(email)
        response = make_response(
            jsonify({"email": f"{email}", "message": "logged in"}))
        session_id = AUTH.create_session(email)
        response.set_cookie("session_id", session_id)
        return response, 200

    abort(401)


@app.route('/sessions', methods=["DELETE"], strict_slashes=False)
def logout():
    """Logs out a user"""
    cookie = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(cookie)
    if user:
        AUTH.destroy_session(user.id)
        redirect('/')
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
