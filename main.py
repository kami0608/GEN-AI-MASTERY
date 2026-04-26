from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    roll_no: int
    grade: str

fake_items=[{"name":"item1","roll_no":1,"grade":"A"},{"name":"item2","roll_no":2,"grade":"B"}]


@app.post('/items/')
def create_item(item:Item):
    return {'name':item.name,'roll_no':item.roll_no,'grade':item.grade}

@app.get('/items/{item_id}')
def read_item(item_id:str):
    return {'item_id':item_id}

@app.get('/')
def main_page():
    return {"message":"welcome to fastapi"}

@app.get("/items/")
def read_items(skip:int=0, limit:int=10):
    return fake_items[skip:skip+limit] 