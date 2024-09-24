#!/usr/bin/env python3
"""A flask application"""
from flask import Flask, jsonify, request, abort, make_response, \
    redirect
from auth import Auth


AUTH = Auth()
app = Flask(__name__)


@app.route('/')
def index():
    """Index route"""
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=["POST"], strict_slashes=False)
def users():
    """Register a user"""
    email = request.form.get("email")
    password = request.form.get("password")

    # if not email or not password:
    #     return jsonify({"message": "email already registered"}), 400

    try:
        AUTH.register_user(email, password)
        return jsonify(
            {"email": f"{email}", "message": "user created"}), 200
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
    if not cookie:
        return abort(403)
    user = AUTH.get_user_from_session_id(cookie)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    return abort(403)


@app.route('/profile', methods=["GET"], strict_slashes=False)
def profile():
    """Retrives a user's profile"""
    cookie = request.cookies.get("session_id")
    if not cookie:
        return abort(403)
    user = AUTH.get_user_from_session_id(cookie)
    if not user:
        return abort(403)
    return jsonify({"email": f"{user.email}"})


@app.route('/reset_password', methods=["POST"], strict_slashes=False)
def reset_password():
    """Reset a user's password"""
    email = request.form.get("email")
    if not email:
        return abort(403)
    user = AUTH.create_session(email)
    if not user:
        abort(403)

    token = AUTH.get_reset_password_token(email)
    if not token:
        return abort(403)
    return jsonify(
        {"email": f"{email}", "reset_token": f"{token}"}), 200


@app.route('/reset_password', methods=["PUT"], strict_slashes=False)
def update_password():
    """Update user password"""
    email = request.form.get("email")
    reset_token = request.form.get("reset_token")
    new_password = request.form.get("new_password")
    # session = AUTH.create_session(email)
    # if not session:
    #     return abort(403)

    try:
        AUTH.update_password(reset_token, new_password)
        return jsonify(
            {"email": f"{email}", "message": "Password updated"}
        ), 200
    except ValueError:
        return abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
