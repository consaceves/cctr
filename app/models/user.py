from .. import db
from sqlalchemy import Column, String, Integer


class User(db.Model):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    dissability = Column(String(100), nullable=False)