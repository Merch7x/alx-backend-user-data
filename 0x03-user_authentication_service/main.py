#!/usr/bin/env python3
"""End to End Integration test"""
import requests


def register_user(email: str, password: str) -> None:
    """Test a user can be registered"""
    params = {"email": f"{email}", "password": f"{password}"}
    response = requests.post(
        'http://127.0.0.1:5000/users', data=params)
    assert response.json() == {"email": f"{email}", "message": "user created"}
    assert response.status_code == 200


def log_in_wrong_password(email: str, password: str) -> None:
    """Evaluate wrong password login"""
    params = {"email": f"{email}", "password": f"{password}"}
    response = requests.post(
        'http://127.0.0.1:5000/sessions', data=params)

    assert response.status_code == 401


def log_in(email: str, password: str) -> str:
    """Test user login"""
    params = {"email": f"{email}", "password": f"{password}"}
    response = requests.post(
        'http://127.0.0.1:5000/sessions', data=params)
    assert response.json() == {"email": f"{email}", "message": "logged in"}
    assert response.status_code == 200

    return response.cookies.get('session_id')


def profile_unlogged() -> None:
    """Test a profile endpoint when user is not logged in"""
    response = requests.get(
        'http://127.0.0.1:5000/profile')
    assert response.status_code == 403


def profile_logged(session_id: str) -> None:
    """Test user profile while logged in"""
    cookie = {"session_id": f"{session_id}"}
    response = requests.get(
        'http://127.0.0.1:5000/profile', cookies=cookie)

    response_data = response.json()
    email = response_data['email']
    assert response_data == {"email": f"{email}"}
    assert response.status_code == 200


def log_out(session_id: str) -> None:
    """Test logging out endpoint"""
    params = {"session_id": f"{session_id}"}
    response = requests.delete(
        'http://127.0.0.1:5000/sessions', data=params)
    assert response.status_code == 403


def reset_password_token(email: str) -> str:
    """Test reset password functionality"""
    params = {"email": f"{email}"}
    response = requests.post(
        'http://127.0.0.1:5000/reset_password', data=params)

    response_data = response.json()
    token = response_data['reset_token']
    assert response.json() == {"email": f"{email}", "reset_token": f"{token}"}
    assert response.status_code == 200
    return token


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Test user password update"""
    params = {
        "email": f"{email}", "reset_token": f"{reset_token}",
        "new_password": f"{new_password}"}
    response = requests.put(
        'http://127.0.0.1:5000/reset_password', data=params)
    assert response.json() == {"email": f"{email}",
                               "message": "Password updated"}
    assert response.status_code == 200


EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
