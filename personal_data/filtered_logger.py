#!/usr/bin/env python3
"""Module for filtering sensitive information from log messages."""

import re


def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    """
    Obfuscates specified fields in the log message.
    
    Args:
        fields: List of strings representing fields to obfuscate
        redaction: String to replace sensitive information with
        message: String representing the log line
        separator: String representing the separator between fields
    
    Returns:
        String with sensitive information obfuscated
    """
    for field in fields:
        pattern = f"(?<={field}=)[^{separator}]*"
        message = re.sub(pattern, redaction, message)
    return message