# app/blog.py
from typing import List # Info: Typing is by-default included in python 3.10+
from fastapi import APIRouter, status, HTTPException
from app.pydantic_objects.blog import Blog as BlogBase
from app.models.user import User
from app.controllers.BaseController import Session, get_db, Depends
from app.models.blog import Blog
from app.serializers.BlogSerializer import BlogSerializer

router = APIRouter()

@router.get('/{id}/blogs', response_model = List[BlogSerializer], response_model_exclude={'creator'})
def index(id, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == id).first()

  if not user:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with {id} not found")
  return user.blogs
