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
