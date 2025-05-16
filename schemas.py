"""
Schemas é fazendo o esquela do banco de dados
seus contrator seus schemas do banco com suas regras
uma tabela de banco de dados tem um schema, mas esses schemas 
não contem dados
"""

from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    

class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserDB(UserSchema):
    id: int

# Criando validação de segurança (returnando sem a senha)
class UserPublic(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserList(BaseModel):
    users: list[UserPublic]