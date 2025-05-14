from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


# Criando validação de segurança (returnando sem a senha)
class UserPublic(BaseModel):
    username: str
    email: EmailStr