from fastapi import FastAPI,UploadFile,Form,Response
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated

import sqlite3

con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()
cur.execute(f"""
            CREATE TABLE IF NOT EXISTS items (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                image BLOB,
                price INTEGER NOT NULL,
                description TEXT,
                place TEXT NOT NULL,
                insertAt INTEGER NOT NULL
            );
            """)

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
async def create_item(image:UploadFile,
                title:Annotated[str,Form()], 
                price:Annotated[int,Form()], 
                description:Annotated[str,Form()], 
                place:Annotated[str,Form()],
                insertAt:Annotated[int,Form()]
                ):
                
    image_bytes = await image.read() # 이미지를 읽는다
    cur.execute(f"""
                INSERT INTO items(title, image, price, description, place, insertAt)
                VALUES ('{title}', '{image_bytes.hex()}',{price}, '{description}', '{place}', {insertAt})
                """) #이미지를 hex 16진법으로
    con.commit()
    return '200'

@app.get("/item")
async def read_item():
    con.row_factory = sqlite3.Row # 컬럼명도 같이 가져옴
    cur = con.cursor() # con의 위치 업데이트
    rows = cur.execute(f"""
                       SELECT * FROM items
                       """).fetchall()
    # return JSONResponse(rows) -> list 형태가 감
    return JSONResponse(jsonable_encoder(dict(row) for row in rows)) #json 으로 바꿔서 encoder -> response 응답

@app.get("/images/{item_id}")
def read_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute(f"""
                              SELECT image FROM items WHERE id={item_id}
                              """).fetchone()[0]
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')

@app.post("/signup")
def signup(id:Annotated[str,Form()], password:Annotated[str,Form()]):
    print(id, password)
    return '200'


app.mount("/", StaticFiles(directory="static", html=True), name="static")