from datetime import datetime
from pathlib import Path

class BaseModel:
    BASE_DIR = Path(__file__).resolve().parent.parent
    DB_DIR = BASE_DIR / 'db'
    def save(self):
        tablePath = Path(self.DB_DIR / f'{self.__class__.__name__}.txt')
        if not tablePath.exists():
            tablePath.touch()
        with open(tablePath, 'a') as arq:
            arq.write(" | ".join(map(str, self.__dict__.values())))
            arq.write('\n')
    
    @classmethod
    def get(cls):
        tablePath = Path(cls.DB_DIR / f'{cls.__name__}.txt')
        if not tablePath.exists():
            tablePath.touch()
        with open(tablePath, 'r') as arq:
            x = arq.readlines()
        results = []
        atributos = vars(cls())
        for i in x:
            split_v = (i.split('|'))
            tmp_dict = dict(zip(atributos, split_v))
            results.append(tmp_dict)
        return results

class Password(BaseModel):
    def __init__(self, domain=None, password=None, expire=False):
        self.domain = domain
        self.password = password
        self.create_at = datetime.now().isoformat()


