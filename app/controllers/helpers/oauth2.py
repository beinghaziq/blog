from fastapi import Depends, HTTPException, status, Request
from fastapi.security import OAuth2PasswordBearer
from app.services import jwt

# login is the session's route name
oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')
def get_current_user(token: str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
)

    return jwt.verify_token(token, credentials_exception)

# TODO: Update all thses when i'll use HTTP only cookies

# def get_current_user_from_headers(request: Request):
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )
#     print(request.headers)

#     return 
