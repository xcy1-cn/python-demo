# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
#
# app = FastAPI()
#
# origins = [
#     "http://localhost:5173",
#     "http://127.0.0.1:5173",
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
#
#
# class LoginForm(BaseModel):
#     username: str
#     password: str
#
#
# @app.get("/")
# async def root():
#     return {"message": "FastAPI 服务已启动"}
#
#
# @app.post("/api/login")
# async def login(data: LoginForm):
#     if data.username == "admin" and data.password == "123456":
#         return {
#             "code": 200,
#             "message": "登录成功",
#             "token": "mock-token-123"
#         }
#     return {
#         "code": 401,
#         "message": "账号或密码错误"
#     }

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatBody(BaseModel):
    message: str


@app.get("/")
async def root():
    return {"message": "FastAPI 服务已启动"}


@app.post("/api/chat")
async def chat(data: ChatBody):
    user_msg = data.message

    # 先写死模拟回复，后面再接真实 AI
    # 替换成真实模型调用
    return {
        "code": 200,
        "reply": f"AI回复：你刚才说的是『{user_msg}』"
    }