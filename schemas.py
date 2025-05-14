from pydantic import BaseModel, EmailStr


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