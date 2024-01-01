from fastapi import status, HTTPException
from sqlalchemy.orm import Session
from database import get_db

class BaseRepository():
	def __init__(self, model) -> None:
		self.db: Session = get_db().__next__()
		self.model = model

	def all(self):
		records = self.db.query(self.model).all()
		return records

	def create(self, record):
		new_record = self.model(**record.__dict__)
		self.db.add(new_record)
		self.db.commit()
		self.db.refresh(new_record)
		return new_record

	def find(self, id):
		record = self.db.query(self.model).filter(self.model.id == id).first()

		if not record:
			raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"{self.model.__name__} with {id} not found")
		return record

	def destroy(self, id):
		record = self.find(id)
		self.db.delete(record)
		self.db.commit()

	def update(self, id, record):
		record_to_update = self.find(id)
		for key, value in record.dict().items():
			setattr(record_to_update, key, value)

		self.db.commit()
		self.db.refresh(record_to_update)
		return record_to_update
	
	def find_by(self, field_name, field_value):
		record = self.db.query(self.model).filter(
			getattr(self.model, field_name) == field_value).first()

		if not record:
			raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
			                    detail=f"{self.model.__name__} with {field_value} not found")
		return record
