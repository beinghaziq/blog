from http.client import HTTPException
from fastapi import APIRouter, status
from app.pydantic_objects.user import User as UserBase
from app.controllers.BaseController import Session, get_db, Depends
from app.models.user import User
from app.serializers.UserSerializer import UserSerializer
from app.services.text_transformer import TextTransformer

router = APIRouter()

@router.post('/', status_code = status.HTTP_201_CREATED, response_model=UserSerializer)
def create(user: UserBase, db: Session = Depends(get_db)):
  new_user = User(name = user.name, email = user.email, password = TextTransformer(user.password).encrypt())
  db.add(new_user)
  db.commit()
  db.refresh(new_user)
  return new_user

@router.get('/{id}', status_code = status.HTTP_200_OK, response_model=UserSerializer)
def show(id, db: Session = Depends(get_db)):
  user = db.query(User).filter(User.id == id).first()

  if not user:
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"User with {id} not found")
  return user
