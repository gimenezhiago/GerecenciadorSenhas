from datetime import datetime
from pathlib import Path
class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DB_DIR = BASE_DIR / 'db'
    def save(self):
        tablePath = Path(self.DB_DIR / 'Password.txt')
        print(self.__class__)
        


class Password(BaseModel):
    def __init__(self, domain=None, password=None, expire=False):
        self.domain = domain
        self.password = password
        self.create_at = datetime.now().isoformat()


