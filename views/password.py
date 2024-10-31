import string, secrets
import hashlib 
import base64
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken


class FernetHasher: 
    RANDOM_STRING_CHARS = string.ascii_lowercase + string.ascii_uppercase
    BASE_DIR = Path(__file__).resolve().parent.parent
    KEY_DIR = BASE_DIR / 'keys'

    def __init__(self, key):
        if not isinstance(key, bytes):
            key = key.encode()

        self.fernet = Fernet(key)

    @classmethod
    def getRandomString(cls, lenght=8):
        string = ''
        for i in range(lenght):
            string = string + secrets.choice(cls.RANDOM_STRING_CHARS)
        return string

    @classmethod
    def createKey(cls, archive=False):
        value = cls.getRandomString()
        hasher = hashlib.sha256(value.encode('utf-8')).digest()
        key = base64.b64encode(hasher)
        if archive:
            return key, cls.arquiveKey(key)
        return key, None

    @classmethod
    def arquiveKey(cls, key):
        file = 'key.key'
        while(Path(cls.KEY_DIR / file).exists()):
            file = f'key_{cls.getRandomString(lenght=5)}.key'
        
        with open(cls.KEY_DIR / file, 'wb') as arq:
            arq.write(key)

        return cls.KEY_DIR / file


    def encrypt(self, value):
        if not isinstance(value, bytes):
            value = value.encode()
        return self.fernet.encrypt(value)

    def decrypt(self, value):
         if not isinstance(value, bytes):
            value = value.encode()
        try:
            return self.fernet.decrypt(value).decode()
        except InvalidToken as e:
            return 'Token inválido'