# app/blog.py
from typing import List # Info: Typing is by-default included in python 3.10+
from fastapi import APIRouter
from app.serializers.BlogSerializer import BlogSerializer
from app.repositories.user_repository import UserRepository

router = APIRouter()
user_repo = UserRepository()

@router.get('/{id}/blogs', response_model = List[BlogSerializer], response_model_exclude={'creator'})
def index(id):
  user = user_repo.find(id)
  return user.blogs
