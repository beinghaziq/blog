from pydantic import BaseModel

class UserSerializer(BaseModel):
  id: int
  name: str
  email: str

  class Config():
    orm_mode = True