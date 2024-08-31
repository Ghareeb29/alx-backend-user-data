# 0x00-personal_data

## Task 0

This function does the following:

1. It uses `re.sub()` to perform the substitution with a single regex.
2. The regex pattern `f'({"|".join(fields)})=[^{separator}]*'` matches any of the specified fields followed by an equals sign and any characters up to the next separator.
3. The replacement `f'\\1={redaction}'` keeps the field name (captured group) and replaces the value with the redaction string.
