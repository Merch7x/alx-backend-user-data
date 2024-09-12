#!/usr/bin/env python3
"""filters logs"""
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns an obfuscated logline"""
    for field in fields:
      message = re.sub(rf'{field}=[^{separator}]*', f'{field}={redaction}', message)
    return message
