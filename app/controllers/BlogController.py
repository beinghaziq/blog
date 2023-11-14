# app/blog.py
from fastapi import APIRouter
from app.pydantic_objects.blog import Blog as BlogBase
from app.controllers.BaseController import Session, get_db, Depends
from app.models.blog import Blog

router = APIRouter()

@router.get('/')
def index(db: Session = Depends(get_db)):
    blogs = db.query(Blog).all()
    return blogs

@router.post('/')
def create(blog: BlogBase, db: Session = Depends(get_db)):
    new_blog = Blog(title = blog.title, body = blog.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
    
@router.get('/{id}')
def show(id, db: Session = Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog
    