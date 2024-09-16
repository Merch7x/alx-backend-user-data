# Project: 0x01. Basic authentication

<h2>Learning Objectives</h2>

<h3>General</h3>

<ul>
<li>What authentication means</li>
<li>What Base64 is</li>
<li>How to encode a string in Base64</li>
<li>What Basic authentication means</li>
<li>How to send the Authorization header</li>
</ul>

<h2>Tasks</h2>

| Task | File |
| ---- | ---- |
| 0. Simple-basic-API | [api/v1/app.py, api/v1/views/index.py](./api/v1/app.py, api/v1/views/index.py) |
| 1. Error handler: Unauthorized | [api/v1/app.py, api/v1/views/index.py](./api/v1/app.py, api/v1/views/index.py) |
| 2. Error handler: Forbidden | [api/v1/auth, api/v1/auth/__init__.py, api/v1/auth/auth.py](./api/v1/auth, api/v1/auth/__init__.py, api/v1/auth/auth.py) |
| 3. Auth class | [api/v1/auth/auth.py](./api/v1/auth/auth.py) |
| 4. Define which routes don't need authentication | [api/v1/app.py, api/v1/auth/auth.py](./api/v1/app.py, api/v1/auth/auth.py) |
| 5. Request validation! | [api/v1/app.py, api/v1/auth/basic_auth.py](./api/v1/app.py, api/v1/auth/basic_auth.py) |
| 6. Basic auth | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) |
| 7. Basic - Base64 part | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) |
| 8. Basic - Base64 decode | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) |
| 9. Basic - User credentials | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) |
| 10. Basic - User object | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) |
| 11. Basic - Overload current_user - and BOOM! | [api/v1/auth/basic_auth.py](./api/v1/auth/basic_auth.py) |
| 12. Basic - Allow password with ":" | [api/v1/auth/auth.py](./api/v1/auth/auth.py) |

