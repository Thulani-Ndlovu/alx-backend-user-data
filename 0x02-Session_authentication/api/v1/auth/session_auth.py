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
