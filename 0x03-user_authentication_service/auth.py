#!/usr/bin/env python3
"""4. Hash password"""
import bcrypt


def _hash_password(password) -> str:
    """Method to hash a password using bcrypt module."""
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
