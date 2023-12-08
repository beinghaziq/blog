from fastapi import status, HTTPException
from app.models.blog import Blog
from sqlalchemy.orm import Session

def all(db=Session):
	blogs = db.query(Blog).all()
	return blogs

def create(blog):
	new_blog = Blog(title = blog.title, body = blog.body, user_id = 1)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)
	return new_blog

def find(id):
	blog = db.query(Blog).filter(Blog.id == id).first()

	if not blog:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with {id} not found")

def destroy(id):
	blog = find(id)
	db.delete(blog)
	db.commit()

def update(blog):
	blog_to_update = find(id)
	for key, value in blog.dict().items():
		setattr(blog_to_update, key, value)

	db.commit()
	db.refresh(blog_to_update)
	return blog_to_update