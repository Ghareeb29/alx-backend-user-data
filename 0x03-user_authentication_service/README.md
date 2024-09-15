# 0x03-user_authentication_service

## Task 1

This implementation does the following:

It adds the add_user method to the DB class with the required parameters: email and hashed_password.
The method creates a new User object with the provided email and hashed password.
It adds the new user to the session and commits the changes to the database.
If the commit is successful, it returns the newly created User object.
If there's an InvalidRequestError (which could happen if there's a problem with the data), it rolls back the session and re-raises the error.
For any other exception, it rolls back the session and raises a ValueError with a descriptive message.

## Task 2

This implementation does the following:

It adds the find_user_by method to the DB class, which takes arbitrary keyword arguments.
The method uses these keyword arguments to filter the query on the User model.
It returns the first user found that matches the query.
If no user is found, it raises a NoResultFound exception.
If invalid query arguments are passed, it allows the InvalidRequestError to be raised.
