# 0x02-Session_authentication

## Task 0

These changes implement the new /users/me endpoint and update the existing GET /api/v1/users/<user_id> route to handle the "me" case. The @app.before_request decorator in app.py now assigns the result of auth.current_user(request) to request.current_user, which is then used in the users.py file to retrieve the authenticated user when "me" is specified as the user_id.
