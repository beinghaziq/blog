from fastapi import FastAPI
from app.controllers.BlogController import router as blog_router

app = FastAPI()

app.include_router(blog_router, prefix='/blog', tags=['blog'])
