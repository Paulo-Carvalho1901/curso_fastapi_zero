from fastapi import FastAPI, status, HTTPException
from schemas import Message, UserDB, UserPublic, UserSchema, UserList

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


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):

    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )

    user_with_id = UserDB(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id

    return user_with_id

@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id : int):
    if user_id < 1 or user_id > len(database):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='User not found'
        )
    
    del database[user_id - 1]

    return {'message': 'User deleted'}





if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', 
            port=8000, log_level='info', reload=True)
