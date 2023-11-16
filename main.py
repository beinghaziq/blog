from fastapi import FastAPI
from app.controllers.BlogController import router as blog_router
from database import engine, Base
from app.models.blog import Blog

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(blog_router, prefix='/blog', tags=['blog'])
