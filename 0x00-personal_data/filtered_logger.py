#!/usr/bin/env python3
"""filters personal information in logs"""
import re


def filter_datum(fields, redaction, message, separator):
    """Returns an obfuscated logline"""
    pattern = '|'.join([f'{field}=[^{separator}]*' for field in fields])
    return re.sub(pattern, lambda match:
                  f'{match.group(0).split("=")[0]}={redaction}', message)
