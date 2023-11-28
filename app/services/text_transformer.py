from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

class TextTransformer:
  def __init__(self, str):
    self.str = str

  def encrypt(self):
    return pwd_context.hash(self.str)
