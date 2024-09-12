#!/usr/bin/env python3
"""filters personal information in logs"""
import re
import logging
from typing import List
import os
import mysql.connector
from mysql.connector import MySQLConnection


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


def get_db() -> MySQLConnection:
    """Returns a connector to the database"""
    host = os.environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    database = os.environ.get("PERSONAL_DATA_DB_NAME")
    user = os.environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = os.environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        port=3306,
        password=password
    )
    return connection


def main() -> None:
    """Retrives and filter data"""
    cursor = get_db().cursor()
    cursor.execute("SELECT * FROM users")
    result = cursor.fetchall()

    for row in result:
        frow = filter_datum(PII_FIELDS, "***", row, ";")
        print(frow)
    cursor.close()


if __name__ == '__main__':
    main()
