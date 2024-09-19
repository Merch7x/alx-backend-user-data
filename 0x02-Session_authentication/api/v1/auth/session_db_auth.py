#!/usr/bin/env python3
"""Session id in a db"""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from flask import request
from os import getenv


class SessionDBAuth(SessionExpAuth):
    """Creating and storing session tokens"""

    user = UserSession()

    def create_session(self, user_id=None):
        """Creates and stores new user sessions"""
        session_id = super().create_session(user_id)
        self.user.session_id = session_id
        self.user.user_id = user_id
        self.user.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Returns the User ID by requesting
        UserSession in the database
        """
        session_id = self.user.session_id
        if session_id is None or\
                not self.user.search({"session_id": session_id}):
            return None
        user_id = self.user.search({"session_id": session_id})
        return user_id[0]

    def destroy_session(self, request=None):
        """
        Destroys the UserSession
        based on the Session ID from the request cookie
        """
        # if request is None:
        #     return False
        cookie = request.cookies.get(getenv("SESSION_NAME"))

        if cookie == self.user.session_id:
            user_id = self.user.id
            self.user.remove(user_id)
