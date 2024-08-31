# 0x00-personal_data

## Task 0

This function does the following:

1. It uses `re.sub()` to perform the substitution with a single regex.
2. The regex pattern `f'({"|".join(fields)})=[^{separator}]*'` matches any of the specified fields followed by an equals sign and any characters up to the next separator.
3. The replacement `f'\\1={redaction}'` keeps the field name (captured group) and replaces the value with the redaction string.

## Task 1

Here's a breakdown of the changes:

1. In the `__init__` method, we now store the `fields` argument as an instance variable.
2. In the `format` method:
   - We use `filter_datum` to redact the sensitive information in the log message.
   - We update `record.msg` with the filtered message.
   - We then call the parent class's `format` method to handle the rest of the formatting.

## Task 2

1. We've added the `PII_FIELDS` tuple at the module level, containing five fields that are considered important Personally Identifiable Information (PII) from the `user_data.csv` file.

2. We've implemented the `get_logger` function:
   - It creates a logger named "user_data".
   - Sets the logging level to INFO.
   - Disables propagation to other loggers.
   - Adds a StreamHandler with the RedactingFormatter, using `PII_FIELDS` to parameterize the formatter.
   - Returns the configured logger.

3. The `get_logger` function is type-annotated to return a `logging.Logger` object.

4. All existing code (filter_datum function and RedactingFormatter class) remains unchanged and compliant with the previously mentioned requirements.

This implementation ensures that when you use the logger returned by `get_logger()`, it will automatically redact the sensitive information specified in `PII_FIELDS` from the log messages.

The `PII_FIELDS` tuple includes five fields that are typically considered sensitive personal information: name, email, phone number, social security number (ssn), and password.

## Task 3

Let's break down the new `get_db` function:

1. We import the necessary modules: `mysql.connector` for database connection and `os` for accessing environment variables.

2. The `get_db` function is implemented:
   - It retrieves database credentials from environment variables using `os.environ.get()`.
   - Default values are set for username ('root'), password (empty string), and host ('localhost').
   - The database name is retrieved from the `PERSONAL_DATA_DB_NAME` environment variable without a default value.
   - It establishes a connection to the MySQL database using `mysql.connector.connect()`.
   - The function is type-annotated to return a `mysql.connector.connection.MySQLConnection` object.

3. The function uses the retrieved credentials to create and return a database connection.

This implementation ensures that:

- Database credentials are never hard-coded in the script.
- The connection is established securely using environment variables.
- Default values are provided for some parameters to ensure the function works even if certain environment variables are not set.

### Fixes

The main changes in the `get_db` function are:

1. We've updated the default password to 'root' instead of an empty string:

   ```python
   password = os.environ.get('PERSONAL_DATA_DB_PASSWORD', 'root')
   ```

2. We've kept the rest of the function the same, as it already aligns with the example provided.

This implementation will work with the MySQL setup described in your example:

- It uses the environment variables `PERSONAL_DATA_DB_USERNAME`, `PERSONAL_DATA_DB_PASSWORD`, `PERSONAL_DATA_DB_HOST`, and `PERSONAL_DATA_DB_NAME` to connect to the database.
- If these environment variables are not set, it will use the default values ('root' for username and password, 'localhost' for host).
- The database name must be provided through the `PERSONAL_DATA_DB_NAME` environment variable.

This setup allows you to run the script as shown in your example:

```bash
PERSONAL_DATA_DB_USERNAME=root PERSONAL_DATA_DB_PASSWORD=root PERSONAL_DATA_DB_HOST=localhost PERSONAL_DATA_DB_NAME=my_db ./main.py
```

And it should correctly connect to the database and execute the query, returning the count of users (2 in your example).
