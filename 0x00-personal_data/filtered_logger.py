#!/usr/bin/env python3
"""filters personal information in logs"""
import re
import logging


def filter_datum(fields, redaction, message, separator):
    """Returns an obfuscated logline
      with select fields obfuscated
    """
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(pattern, lambda match:
                  f'{match.group(0).split("=")[0]}={redaction}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: list[str]):
        """Object initialiser"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats and reducts the recorrd accordingly"""
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
