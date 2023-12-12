# app/models/user.py
from sqlalchemy import Column, Integer, String, func, DateTime
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
  __tablename__ = 'users'

  id = Column(Integer, primary_key=True, index=True)
  email = Column(String)
  name = Column(String)
  password = Column(String)
  blogs = relationship('Blog', back_populates = 'creator')
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())