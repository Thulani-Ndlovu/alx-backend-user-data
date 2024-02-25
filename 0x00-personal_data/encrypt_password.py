#!/usr/bin/env python3
'''Password Encryption'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''hashing using bcrypt'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
