from ., import db
from sqlalchemy import Column, String, Integer
from sqlalchemy_utils import EmailType


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(EmailType(100), nullable=False)