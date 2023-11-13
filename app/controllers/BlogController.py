# app/blog.py
from fastapi import APIRouter
from app.models.blog import Blog

router = APIRouter()

@router.get('/')
def index():
    return 'all Blogs'

@router.post('/')
def create(blog: Blog):
    return blog