from fastapi import FastAPI, status
from schemas import UserSchema, UserPublic, UserDB

# estânciando da classe FastAPI
app = FastAPI(title='Curso FastAPI 2024')

# Criando um  banco de dados em memória
database = []

@app.post('/users/', response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema): # parametro utilizado para trazer o objeto schema definido

    user_with_id = UserDB(
        id=len(database) + 1,
        **user.model_dump()
    )

    database.append(user_with_id)

    return user_with_id




if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)

