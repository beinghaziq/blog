# app/blog.py
from typing import List # Info: Typing is by-default included in python 3.10+
from fastapi import APIRouter, status
from app.pydantic_objects.blog import Blog as BlogBase
from app.repositories.blog_repository import BlogRepository as BlogRepo
from app.serializers.BlogSerializer import BlogSerializer

router = APIRouter()
blog_repo = BlogRepo()

@router.get('/', response_model = List[BlogSerializer])
def index():
	return blog_repo.all()
	
@router.post('/', status_code = status.HTTP_201_CREATED, response_model = BlogSerializer)
def create(blog: BlogBase):
	blog.user_id = 1
	return blog_repo.create(blog)

@router.get('/{id}', status_code = 200, response_model = BlogSerializer)
def show(id):
	return blog_repo.find(id)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int):
  blog_repo.destroy(id)
  return { 'message': 'Blog deleted successfully' }

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model = BlogSerializer)
def update(id: int, blog: BlogBase):
	return blog_repo.update(id, blog)
