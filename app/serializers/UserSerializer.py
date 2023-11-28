from pydantic import BaseModel

class UserSerializer(BaseModel):
  id: int
  name: str
  email: str
