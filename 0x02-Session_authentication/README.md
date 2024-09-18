# Project: 0x02. Session authentication

<h2>Learning Objectives</h2>

<h3>General</h3>

<ul>
<li>What authentication means</li>
<li>What session authentication means</li>
<li>What Cookies are</li>
<li>How to send Cookies</li>
<li>How to parse Cookies</li>
</ul>

<h2>Tasks</h2>

| Task | File |
| ---- | ---- |
| 0. Et moi et moi et moi! | [api/v1/app.py, api/v1/views/users.py](./api/v1/app.py, api/v1/views/users.py) |
| 1. Empty session | [api/v1/auth/session_auth.py, api/v1/app.py](./api/v1/auth/session_auth.py, api/v1/app.py) |
| 2. Create a session | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py) |
| 3. User ID for Session ID | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py) |
| 4. Session cookie | [api/v1/auth/auth.py](./api/v1/auth/auth.py) |
| 5. Before request | [api/v1/app.py](./api/v1/app.py) |
| 6. Use Session ID for identifying a User | [api/v1/auth/session_auth.py](./api/v1/auth/session_auth.py) |
| 7. New view for Session Authentication | [api/v1/views/session_auth.py, api/v1/views/__init__.py](./api/v1/views/session_auth.py, api/v1/views/__init__.py) |
| 8. Logout | [api/v1/auth/session_auth.py, api/v1/views/session_auth.py](./api/v1/auth/session_auth.py, api/v1/views/session_auth.py) |
| 9. Expiration? | [api/v1/auth/session_exp_auth.py, api/v1/app.py](./api/v1/auth/session_exp_auth.py, api/v1/app.py) |
| 10. Sessions in database | [api/v1/auth/session_db_auth.py, api/v1/app.py, models/user_session.py](./api/v1/auth/session_db_auth.py, api/v1/app.py, models/user_session.py) |

