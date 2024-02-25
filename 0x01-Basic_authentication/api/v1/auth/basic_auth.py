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
        if type(authorization_header) is str:
            pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
            return None

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        '''decode base 64 authorization header'''
        if type(base64_authorization_header) is str:
            try:
                res = base64.b64decode(
                    base64_authorization_header,
                    validate=True,
                )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None
