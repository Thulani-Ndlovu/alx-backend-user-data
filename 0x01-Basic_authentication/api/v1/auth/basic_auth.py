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

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        '''user credentials extraction'''
        if type(decoded_base64_authorization_header) is str:
            pattern = r'(?P<user>[^:]+):(?P<password>.+)'
            field_match = re.fullmatch(
                pattern,
                decoded_base64_authorization_header.strip(),
            )
            if field_match is not None:
                user = field_match.group('user')
                password = field_match.group('password')
                return user, password
        return None, None

    def user_object_from_credentials(
            self,
            user_email: str, user_pwd: str) -> TypeVar('User'):
        '''get user object from credentials'''
        if type(user_email) is str and type(user_email) is str:
            try:
                users = User.search({"email": user_email})
            except Exception:
                return None
            if len(users) <= 0:
                return None
            if users[0].is_valid_password(user_pwd):
                return users[0]
        return None
