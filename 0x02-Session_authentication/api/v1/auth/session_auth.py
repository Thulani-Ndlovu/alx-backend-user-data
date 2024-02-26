#!/usr/bin/env python3
'''session authentication'''
from uuid import uuid4
from flask import request

from .auth import Auth
from models.user import User


class SessionAuth(Auth):
    '''SessionAuth Class'''
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        '''creating user session'''
        if type(user_id) is str:
            session_id = str(uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        '''get user id with a certain session id'''
        if type(session_id) is str:
            return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        '''returns user instance based on a cookie value'''
        user_id = self.user_id_for_session_id(self.session_cookie(request))
        return User.get(user_id)
