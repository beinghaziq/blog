from app.repositories.base_repository import BaseRepository
from app.models.blog import Blog

class BlogRepository(BaseRepository):
	def __init__(self) -> None:
		super().__init__(Blog)
