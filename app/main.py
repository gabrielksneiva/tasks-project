from fastapi import FastAPI, APIRouter
from app.mongodb import get_data, delete_data, update_data, insert_data, show_all_data

app = FastAPI()

@app.get('/healthcheck')
async def healthcheck():
    return {"message":"ok"}


@app.get('/get_task')
async def get_task(task: str):
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
async def get_task(task: str):
        data = insert_data(task)
        return data

@app.post('/update_task')
async def get_task(task: str, new_task: str):
        data = update_data(task, new_task)
        return data

    
@app.delete('/delete_task')
async def get_task(task: str):
        data = delete_data(task)
        return data
