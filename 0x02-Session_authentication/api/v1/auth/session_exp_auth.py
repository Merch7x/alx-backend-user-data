#!/usr/bin/env python3
"""Work on timeouts for sessions"""
from api.v1.auth.session_auth import SessionAuth
from os import getenv
from datetime import datetime, timedelta


class SessionExpAuth(SessionAuth):
    """Adds an expiration to a sessionId"""

    def __init__(self, session_duration: int = None):
        """Intialize an object"""
        if session_duration is None:
            session_duration = int(getenv("SESSION_DURATION"))
        self.session_duration = session_duration

    def create_session(self, user_id=None):
        """Recreate session id storage
            by adding a datetime object
            in the dict
        """
        sesh_id = super().create_session(user_id)
        if sesh_id is None:
            return None
        session_dictionary = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        super().user_id_by_session_id[sesh_id] =\
            session_dictionary
        return sesh_id

    def user_id_for_session_id(self, session_id=None):
        """retrives user_id from session dict"""
        if session_id is None or\
                not super().user_id_by_session_id.get(session_id):
            return None
        session_dict = super().user_id_by_session_id.get(session_id)
        if self.session_duration <= 0:
            return session_dict.get("user_id")

        if not session_dict.get("created_at"):
            return None

        exp_time = session_dict.get("created_at") +\
            timedelta(seconds=self.session_duration)

        if datetime.now() > exp_time:
            return None
        return session_dict.get("user_id")
