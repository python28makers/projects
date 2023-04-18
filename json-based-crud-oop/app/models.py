from dataclasses import dataclass, asdict
from uuid import UUID

class Model:
    def dict(self):
        return asdict(self)
    

@dataclass
class User(Model):
    uid: UUID # уникальный идентификатор
    username: str
    age: int
    email: str
    
# u1 = User('13', 'Alex', 13, 'alex@gmail.com')
# asdict(u1) -> {"name": "Alex", "age": 13, "email": "alex@gmail.com"}