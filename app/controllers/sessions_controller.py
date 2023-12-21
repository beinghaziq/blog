from fastapi import APIRouter, status, HTTPException
from app.pydantic_objects.login import Login
from app.repositories.user_repository import UserRepository
from app.services.text_transformer import TextTransformer
from app.services import jwt

router = APIRouter()
user_repo = UserRepository()

@router.post('/login')
def create(request: Login):
	user = user_repo.find_by('email', request.username)
	if not TextTransformer(request.password, user.password).verify():
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"password incorrect")
	
	token = jwt.create_access_token(data={ 'sub': user.email })
	return { 'access_token': token, 'token_type': 'bearer' }
