from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class info(BaseModel):
    start_lat : int
    start_lon : int
    end_lat : int
    end_lon : int

@app.get('/', status_code=200)
def index():
    return {'message': 'hello world!'}

@app.post('/', status_code=201)
def index_post(info: info):
    print(info)
    return info

@app.options('/')
def index_options(info: info):
    print(info)
    return info



if __name__ == '__main__':
    uvicorn.run(
        "app:app",
        host="localhost",
        port=5000,
        reload=True
    )