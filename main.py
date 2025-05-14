from fastapi import FastAPI, status
from schemas import UserDB, UserPublic, UserSchema

# estânciando da classe FastAPI
app = FastAPI(title='Curso FastAPI 2024')

# Criando um  banco de dados em memória
database = []

@app.post('/users/', response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema): # parametro utilizado para trazer o objeto schema definido

    user_with_id = UserDB(
        id=len(database) + 1, # encrementando em 1 id no banco em memoria
        **user.model_dump() # (**user desenpacotamento não nomeado) model_dump(Transformando o dado em dicionario)
    )

    database.append(user_with_id) # fazendo o db recebendo os user criados

    return user_with_id



if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)

