from fastapi import FastAPI, status
from schemas import UserSchema, UserPublic

# estânciando da classe FastAPI
app = FastAPI(title='Curso FastAPI 2024')


@app.post('/users/', response_model=UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(user: UserSchema): # parametro utilizado para trazer o objeto schema definido
    return user




if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)

