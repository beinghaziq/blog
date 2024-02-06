# app/models/blog.py
from sqlalchemy import Column, Integer, String, ForeignKey, func, DateTime
from database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
	__tablename__ = 'blogs'

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String)
	body = Column(String)
	user_id = Column(Integer, ForeignKey('users.id'))
	creator = relationship('User', back_populates = 'blogs')
	created_at = Column(DateTime(timezone=True), server_default=func.now())
	updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

	def __repr__(self):
		attributes = ', '.join(f"{key}={repr(value)}" for key, value in vars(self).items())
		return f"{self.__class__.__name__}({attributes})"
