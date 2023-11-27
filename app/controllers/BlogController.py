# app/blog.py
from typing import List
from fastapi import APIRouter, status, HTTPException
from app.pydantic_objects.blog import Blog as BlogBase
from app.controllers.BaseController import Session, get_db, Depends
from app.models.blog import Blog
from app.serializers.BlogSerializer import BlogSerializer

router = APIRouter()

@router.get('/', response_model = List[BlogSerializer])
def index(db: Session = Depends(get_db)):
	blogs = db.query(Blog).all()
	return blogs
	

@router.post('/', status_code = status.HTTP_201_CREATED, response_model = BlogSerializer)
def create(blog: BlogBase, db: Session = Depends(get_db)):
	new_blog = Blog(title = blog.title, body = blog.body)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)
	return new_blog


@router.get('/{id}', status_code = 200, response_model = BlogSerializer)
def show(id, db: Session = Depends(get_db)):
	blog = db.query(Blog).filter(Blog.id == id).first()

	if not blog:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with {id} not found")
	return blog


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
  blog = db.query(Blog).filter(Blog.id == id).first()

  if not blog:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Blog not found")

  db.delete(blog)
  db.commit()
    
  return { "message": "Blog deleted successfully" }


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model = BlogSerializer)
def update(id: int, blog: BlogBase, db: Session = Depends(get_db)):
	blog_to_update = db.query(Blog).filter(Blog.id == id).first()
	
	if not blog_to_update:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = "Blog not found") 

	for key, value in blog.dict().items():
		setattr(blog_to_update, key, value)

	db.commit()
	db.refresh(blog_to_update)
	
	return blog_to_update
