#!/usr/bin/env python3
"""filters personal information in logs"""
import re
import logging
from typing import List


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns an obfuscated logline"""
    for field in fields:
        res = re.sub(rf'{field}=[^{separator}]*',
                     f'{field}={redaction}', message)
    return res


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

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
