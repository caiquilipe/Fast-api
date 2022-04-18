from typing import Optional
from pydantic import BaseModel, EmailStr

class User(BaseModel):
    username: str
    password: str
    first_name: Optional[str]
    last_name: Optional[str]
    email: EmailStr
    cpf: str
    