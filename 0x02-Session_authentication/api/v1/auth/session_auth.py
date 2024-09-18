"""Working on session based authentication"""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session based Authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates user session"""
        if user_id is None or not isinstance(user_id, str):
            return None
        session_id = uuid.uuid4()
        self.user_id_by_session_id[str(session_id)] = user_id
        return session_id
