from fastapi import FastAPI,UploadFile,Form
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from pydantic import BaseModel
import sqlite3

# con = sqlite3.connect('db.db', check_same_thread=False)
# cur = con.cursor()

app = FastAPI()

# @app.post("/items")
# async def create_item(image:UploadFile, 
#                 title:Annotated[str,Form()], 
#                 price:Annotated[int,Form()],
#                 description:Annotated[str,Form()],
#                 place:Annotated[str,Form()],
#                 insertAt:Annotated[int,Form()]):
#     # print(image, title, price,description,place)
    
#     image_bytes = await image.read()
#     cur.execute(f"""
#                 INSERT INTO items(title, image, price, description, place, insertAt)
#                 VALUES ('{title}','{image_bytes.hex()}',{price},'{description}','{place}',{insertAt})
#                 """)
#     con.commit()
    
#     return'200'

# @app.get("/items")
# async def get_items() :
#     # 컬럼명도 같이 가져옴
#     con.row_factory = sqlite3.Row
    
#     rows = cur.execute(f"""
#                        SELECT * from items;
#                        """).fetchall()
    
#     return JSONResponse(rows)



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

app.mount("/", StaticFiles(directory="static", html=True), name="static")