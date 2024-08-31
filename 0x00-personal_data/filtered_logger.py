#!/usr/bin/env python3
"""
This module provides utilities for filtering and formatting log messages,
including functions to obfuscate sensitive information and a custom
logging formatter.
"""

import re
from typing import List
import logging


# PII fields to be redacted
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """
    Obfuscates specified fields in a log message.

    Args:
        fields: A list of strings representing all fields to obfuscate.
        redaction: A string representing by what the field will be obfuscated.
        message: A string representing the log line.
        separator: A string representing the character separating fields
        in the log line.

    Returns:
        The log message with specified fields obfuscated.
    """
    return re.sub(f'({"|".join(fields)})=[^{separator}]*',
                  f"\\1={redaction}", message)


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class

    This formatter replaces sensitive information
    in log messages with a redaction string.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with fields to redact.

        Args:
            fields: A list of strings representing the fields to redact
            in log messages.
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Format the specified record as text.

        Args:
            record: A LogRecord instance representing the event being logged.

        Returns:
            A formatted string with sensitive information redacted.
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.getMessage(), self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data.

    Returns:
        A logging.Logger object configured to redact sensitive information.
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(PII_FIELDS))

    logger.addHandler(stream_handler)

    return logger
