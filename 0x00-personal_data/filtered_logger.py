#!/usr/bin/env python3
""""filtered_logger.py"""
import re
from typing import List


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str) -> str:
    """ that returns the log message obfuscated:"""
    for fieled in fields:
        message = re.sub(f'{fieled}=(.*?)',
                         f'{fieled}={redaction}{separator}', message)
    return message
