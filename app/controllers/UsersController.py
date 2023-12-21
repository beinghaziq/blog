from fastapi import APIRouter, status
from app.pydantic_objects.user import User as UserBase
from app.serializers.UserSerializer import UserSerializer
from app.services.text_transformer import TextTransformer
from app.repositories.user_repository import UserRepository

router = APIRouter()
user_repo = UserRepository()

# Info: tags=['blog'] can be written here for proper documentation
@router.post('/', status_code = status.HTTP_201_CREATED, response_model=UserSerializer)
def create(user: UserBase):
	user.password = TextTransformer(user.password).encrypt()
	return user_repo.create(user)

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model=UserSerializer)
def show(id):
  return user_repo.find(id)
