#!/usr/bin/env python3
'''API Authentication'''
import re
import os
from flask import request
from typing import List, TypeVar


class Auth:
    '''Authentication class'''
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''authorization request'''
        if path is not None and excluded_paths is not None:
            for ex_path in map(lambda x: x.strip(), excluded_paths):
                pattern = ''
                if ex_path[-1] == '*':
                    pattern = '{}.*'.format(ex_path[0:-1])
                elif ex_path[-1] == '/':
                    pattern = '{}/*'.format(ex_path[0:-1])
                else:
                    pattern = '{}/*'.format(ex_path)
                if re.match(pattern, path):
                    return False
        return True

    def authorization_header(self, request=None) -> str:
        '''authorization header'''
        if request is not None:
            return request.headers.get('Authorization', None)
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        '''current user'''
        return None

    def session_cookie(self, request=None):
        '''gets the cookies of a session'''
        if request is not None:
            cookie_name = os.getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)
