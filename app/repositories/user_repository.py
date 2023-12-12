from app.repositories.base_repository import BaseRepository
from app.models.user import User

class UserRepository(BaseRepository):
	def __init__(self) -> None:
		super().__init__(User)
