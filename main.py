from fastapi import FastAPI
from app.controllers.BlogController import router as blog_router
from app.controllers.UsersController import router as user_router
from database import engine, Base
from app.models.blog import Blog

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(blog_router, prefix='/blog', tags=['blog'])
app.include_router(user_router, prefix='/user', tags=['user'])
