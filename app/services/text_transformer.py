from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated = 'auto')

class TextTransformer:
  def __init__(self, plain_str, hashed_password=None):
    self.plain_str = plain_str
    self.hashed_password = hashed_password

  def encrypt(self):
    return pwd_context.hash(self.plain_str)

  def verify(self):
      return pwd_context.verify(self.plain_str, self.hashed_password)