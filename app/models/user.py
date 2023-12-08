# app/models/user.py
from sqlalchemy import Column, Integer, String
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String)
  name = Column(String)
  password = Column(String)
  blogs = relationship('Blog', back_populates = 'creator')