#!/usr/bin/env python3
"""filters logs"""
import re


def filter_datum(fields: list[str], redaction: str,
                 message: str, separator: str) -> str:
    """Returns an obfuscated logline"""
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(pattern, lambda match:
                  f'{match.group(0).split("=")[0]}={redaction}', message)
