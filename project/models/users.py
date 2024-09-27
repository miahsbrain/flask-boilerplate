from project.extensions import db
from project.models.base import BaseModel
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean
from flask_login import UserMixin

class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    uid = Column(Integer, autoincrement=True, unique=True, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f'<NAME: {self.first_name} {self.last_name}, EMAIL: {self.email}>'
    
    def get_id(self):
        return self.uid
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    

class AnonymousUser(UserMixin):
    uid = '10000000001'
    first_name = 'Anonymous'
    last_name = 'User'

    def __repr__(self) -> str:
        return f'<NAME: {self.first_name} {self.last_name}, EMAIL: {self.email}>'
    
    def get_id(self):
        return self.uid
    
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'