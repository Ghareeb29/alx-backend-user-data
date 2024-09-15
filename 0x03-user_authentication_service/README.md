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

## Task 4

This implementation does the following:

We import the bcrypt module, which we'll use for hashing the password.
We define the _hash_password function that takes a password string as input and returns bytes.
Inside the function:

We convert the input password string to bytes using encode('utf-8').
We generate a salt using bcrypt.gensalt().
We hash the password using bcrypt.hashpw(), which takes the password bytes and the salt as arguments.

Finally, we return the hashed password, which is in bytes format.

## Task 5

This implementation does the following:

We keep the _hash_password function as previously implemented.
In the Auth class:

We implement the register_user method that takes email and password as mandatory arguments.
We first try to find a user with the given email using self._db.find_user_by().
If a user is found (i.e., no exception is raised), we raise a ValueError with the message "User <user's email> already exists".
If NoResultFound is raised (meaning the user doesn't exist), we catch this exception and proceed to create the new user.
We hash the password using the _hash_password function.
We use self._db.add_user() to save the new user to the database.
Finally, we return the newly created User object.
