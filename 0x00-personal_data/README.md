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
