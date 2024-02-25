#!/usr/bin/env python3
'''Password Encryption'''
import bcrypt


def hash_password(password: str) -> bytes:
    '''hashing using bcrypt'''
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    '''password validity'''
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
