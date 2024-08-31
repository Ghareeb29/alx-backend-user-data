#!/usr/bin/env python3
"""
This module provides utilities for filtering and formatting log messages,
including functions to obfuscate sensitive information, a custom
logging formatter, and database connection functionality.
"""

import re
from typing import List
import logging
import mysql.connector
import os


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

    This formatter replaces sensitive information in log messages
    with a redaction string.
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        Initialize the RedactingFormatter with fields to redact.

        Args:
            fields: A list of strings representing the fields
            to redact in log messages.
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


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    Connects to the MySQL database using credentials
    from environment variables.

    Returns:
        A MySQLConnection object connected to the database.
    """
    username = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "root")
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = os.environ.get("PERSONAL_DATA_DB_NAME")

    connection = mysql.connector.connect(
        user=username, password=password, host=host, database=db_name
    )

    return connection


def main() -> None:
    """
    Main function to retrieve and display filtered user data from the database.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    fields = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        str_row = "".join(f"{f}={str(r)}; " for r, f in zip(row, fields))
        logger.info(str_row.strip())

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
