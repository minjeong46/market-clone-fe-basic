from fastapi import FastAPI,UploadFile,Form,Response,Depends
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Annotated
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
import hashlib

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

SECRET = "super-coding"
manager = LoginManager(SECRET, token_url='/login') # login 페이지에서만 사용

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
                insertAt:Annotated[int,Form()],
                user=Depends(manager)
                ):
                
    image_bytes = await image.read() # 이미지를 읽는다
    cur.execute(f"""
                INSERT INTO items(title, image, price, description, place, insertAt)
                VALUES ('{title}', '{image_bytes.hex()}',{price}, '{description}', '{place}', {insertAt})
                """) #이미지를 hex 16진법으로
    con.commit()
    return '200'

@app.get("/item")
async def read_item(user=Depends(manager)): # user 가 인증된 상태에서만 동작
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

@manager.user_loader()
def query_user(data):
    WHERE_STATEMENTS = f'id="{data}"'
    if type(data) == dict:
        WHERE_STATEMENTS = f'''id="{data['id']}"'''
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    user = cur.execute(f"""
                       SELECT * from users WHERE {WHERE_STATEMENTS}
                       """).fetchone()
    return user

@app.post("/login")
def login(id:Annotated[str,Form()], password:Annotated[str,Form()]):
    user = query_user(id)
    if not user:
        raise InvalidCredentialsException # raise 에러메세지, InvalidCredentialsException 401를 자동으로 생성해서 내려줌
    elif password != user['password']:
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(data={
        'sub': user['id'],
    })
    
    return {'access_token': access_token}
    

@app.post("/signup")
def signup(id:Annotated[str,Form()], password:Annotated[str,Form()], name:Annotated[str,Form()], email:Annotated[str,Form()]):
    hash_object = hashlib.sha1(password.encode())
    password_hash = hash_object.hexdigest()
    print(password_hash)
    cur.execute(f"""
                INSERT INTO users(id,password,name,email)
                VALUES ('{id}', '{password_hash}', '{name}', '{email}')
                """)
    con.commit()
    # print(id, password)
    return '200'


app.mount("/", StaticFiles(directory="static", html=True), name="static")