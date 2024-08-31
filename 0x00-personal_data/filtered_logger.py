#!/usr/bin/env python3
"""
This module provides a function to obfuscate sensitive information
in log messages.
"""

import re
from typing import List


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
