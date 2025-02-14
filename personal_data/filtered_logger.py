#!/usr/bin/env python3
"""Module for filtering sensitive information from log messages."""

import logging
import re
from typing import List, Tuple


# PII fields to be redacted
PII_FIELDS: Tuple[str, ...] = ('name', 'email', 'phone', 'ssn', 'password')


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


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Initialize the RedactingFormatter with fields to redact.
        
        Args:
            fields: List of strings representing fields to redact
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record while redacting specified fields.
        
        Args:
            record: LogRecord instance containing the log message
            
        Returns:
            Formatted log message with sensitive information redacted
        """
        record.msg = filter_datum(self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    Creates and configures a logger for user data.
    
    Returns:
        logging.Logger: Configured logger object
    """
    # Create logger
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    # Create and configure stream handler
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))
    
    # Add handler to logger
    logger.addHandler(stream_handler)
    
    return logger