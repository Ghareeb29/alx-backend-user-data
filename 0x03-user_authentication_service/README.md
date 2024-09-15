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

## Task 3

This implementation does the following:

It adds the update_user method to the DB class, which takes a required user_id argument and arbitrary keyword arguments.
The method uses find_user_by to locate the user by ID.
It then iterates through the provided keyword arguments, checking if each corresponds to a valid user attribute using hasattr().
If a valid attribute is found, it updates the user's attribute using setattr().
If an invalid attribute is passed, it raises a ValueError.
After updating all valid attributes, it commits the changes to the database.
If the user is not found, it raises a ValueError.
If there's an InvalidRequestError, it rolls back the session and raises a ValueError.
