from fastapi import status, HTTPException
from app.models.blog import Blog
from sqlalchemy.orm import Session

def all(db=Session):
	blogs = db.query(Blog).all()
	return blogs

def create(blog, db=Session):
	new_blog = Blog(**blog.__dict__, user_id = 1)
	db.add(new_blog)
	db.commit()
	db.refresh(new_blog)
	return new_blog

def find(id, db=Session):
	blog = db.query(Blog).filter(Blog.id == id).first()

	if not blog:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Blog with {id} not found")
	return blog

def destroy(id, db):
	blog = find(id, db)
	db.delete(blog)
	db.commit()

def update(id, blog, db):
	blog_to_update = find(id, db)
	for key, value in blog.dict().items():
		setattr(blog_to_update, key, value)

	db.commit()
	db.refresh(blog_to_update)
	return blog_to_update
