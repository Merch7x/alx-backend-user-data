#!/usr/bin/env python3
"""filters personal information in logs"""
import re
import logging
from typing import List
import os
import mysql.connector


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password',)


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns an obfuscated logline"""
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(pattern, lambda match:
                  f'{match.group(0).split("=")[0]}={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """Object initialiser"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats and reducts the recorrd accordingly"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Creates a logger"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    file_handler = logging.StreamHandler()
    file_handler.setLevel(logging.INFO)
    formatter = RedactingFormatter(PII_FIELDS)
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns a connector to the database"""
    connection = mysql.connector.connect(
        host="localhost" or os.environ.get('PERSONAL_DATA_DB_HOST'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME'),
        user="root" or os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password="" or os.environ.get('PERSONAL_DATA_DB_PASSWORD')
    )
    return connection
