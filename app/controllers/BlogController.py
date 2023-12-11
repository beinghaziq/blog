# app/blog.py
from typing import List # Info: Typing is by-default included in python 3.10+
from fastapi import APIRouter, status, HTTPException
from app.pydantic_objects.blog import Blog as BlogBase
from app.controllers.BaseController import Session, get_db, Depends
from app.models.blog import Blog
import app.repositories.blog as BlogRepo
from app.serializers.BlogSerializer import BlogSerializer

router = APIRouter()

@router.get('/', response_model = List[BlogSerializer])
def index(db: Session = Depends(get_db)):
	return BlogRepo.all(db)
	

@router.post('/', status_code = status.HTTP_201_CREATED, response_model = BlogSerializer)
def create(blog: BlogBase, db: Session = Depends(get_db)):
	return BlogRepo.create(blog, db)

@router.get('/{id}', status_code = 200, response_model = BlogSerializer)
def show(id, db: Session = Depends(get_db)):
	return BlogRepo.find(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
  BlogRepo.destroy(id, db)
  return { "message": "Blog deleted successfully" }


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model = BlogSerializer)
def update(id: int, blog: BlogBase, db: Session = Depends(get_db)):
	return BlogRepo.update(id, blog, db)
