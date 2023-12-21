from fastapi import FastAPI
from app.controllers.BlogController import router as blog_router
from app.controllers.UsersController import router as user_router
from app.controllers.users.blogs_controller import router as user_blogs_router
from app.controllers.sessions_controller import router as session_router
from database import engine, Base

app = FastAPI()

Base.metadata.create_all(engine)
app.include_router(blog_router, prefix='/blog', tags=['blog'])
app.include_router(user_router, prefix='/user', tags=['user'])
app.include_router(user_blogs_router, prefix='/users', tags=['user_blogs'])
app.include_router(session_router, tags=['session'])
