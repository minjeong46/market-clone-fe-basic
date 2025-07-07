from fastapi import FastAPI,UploadFile,Form
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import Annotated


app = FastAPI()

class Msg(BaseModel):
    id: str
    msg: str

msgs = []

@app.post("/chat")
def create_msg(msg:Msg) :
    msgs.append(msg)
    return "성공"
    
@app.get("/chat")
def read_msg() :
    return msgs;

@app.post("/item")
def create_item(image:UploadFile,
                title:Annotated[str,Form()], 
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()], 
                place:Annotated[str,Form()]):
    print(image,title,price,description,place)
    return "200"


app.mount("/", StaticFiles(directory="static", html=True), name="static")