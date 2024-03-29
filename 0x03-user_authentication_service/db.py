#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine, tuple_
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.session import Session


from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        '''Adds a user to the database'''
        try:
            newUser = User(email=email, hashed_password=hashed_password)
            self._session.add(newUser)
            self._session.commit()
        except Exception:
            self._session.rollback()
            newUser = None
        return newUser

    def find_user_by(self, **kwargs) -> User:
        '''Find user by filter'''
        f, vals = [], []
        for key, val in kwargs.items():
            if hasattr(User, key):
                f.append(getattr(User, key))
                vals.append(val)
            else:
                raise InvalidRequestError()
        res = self._session.query(User).filter(
            tuple_(*f).in_([tuple(vals)])
        ).first()
        if res is None:
            raise NoResultFound()
        return res

    def update_user(self, user_id: int, **kwargs) -> None:
        '''update user based on id'''
        _user = self.find_user_by(id=user_id)
        if _user is None:
            return
        updateUser = {}
        for key, val in kwargs.items():
            if hasattr(User, key):
                updateUser[getattr(User, key)] = val
            else:
                raise ValueError()
        self._session.query(User).filter(User.id == user_id).update(
            updateUser,
            synchronize_session=False,
        )
        self._session.commit()
