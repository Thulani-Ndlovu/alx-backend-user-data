#!/usr/bin/env python3
'''Basic Authentication Class'''
import re
import base64
import binascii
from typing import Tuple, TypeVar

from .auth import Auth
from models.user import User


class BasicAuth(Auth):
    '''Basic auth'''
    def extract_base64_authorization_header(
            self,
            authorization_header: str) -> str:
        '''base64 authorization header extraction'''
        if type(authorization_header) == str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
            return None
        