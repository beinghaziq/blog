from fastapi import APIRouter, status, HTTPException, Depends
from app.pydantic_objects.login import Login
from app.repositories.user_repository import UserRepository
from app.services.text_transformer import TextTransformer
from app.services import jwt
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()
user_repo = UserRepository()

@router.post('/login')
def create(request: OAuth2PasswordRequestForm = Depends()):
	user = user_repo.find_by('email', request.username)
	if not TextTransformer(request.password, user.password).verify():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"password incorrect")
	
	token = jwt.create_access_token(data={ 'sub': user.email })
	return { 'access_token': token, 'token_type': 'bearer' }
