from fastapi import FastAPI, APIRouter, HTTPException, Depends
from app.mongodb import get_data, delete_data, update_data, insert_data, show_all_data
from app.autentication import *
from fastapi.security import OAuth2PasswordBearer
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

@app.get('/healthcheck')
async def healthcheck():
    return {"message":"ok"}


@app.get('/get_task')
async def get_task(task: str = Depends(oauth2_scheme)):
        data = get_data(task)
        return data

@app.get('/get_all_tasks')
async def get_task():
        data_out = []
        data = show_all_data()
        for x in data:
               data_out.append(x['task'])
        return {"tasks": data_out}

@app.post('/insert_task')
async def get_task(task: str = Depends(oauth2_scheme)):
        data = insert_data(task)
        return data

@app.post('/update_task')
async def get_task(task: str = Depends(oauth2_scheme), new_task: str = Depends(oauth2_scheme)):
        data = update_data(task, new_task)
        return data

    
@app.delete('/delete_task')
async def get_task(task: str = Depends(oauth2_scheme)):
        data = delete_data(task)
        return data


@app.post("/register")
def register(username: str = Depends(oauth2_scheme), password: str = Depends(oauth2_scheme)):
    hashed_password = hash_password(password)
    # Adicione o novo usuário ao MongoDB
    return {"username": username, "hashed_password": hashed_password}

@app.post("/login")
def login(username: str = Depends(oauth2_scheme), password: str = Depends(oauth2_scheme)):
    # Verifique o usuário e a senha no MongoDB
    user = get_data(username)
    if not user or not verify_password(password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}