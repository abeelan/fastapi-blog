"""
数据库会话中间件
"""

from typing import Callable

from fastapi import FastAPI, Request, Response

from blog.db import SessionFactory


async def db_session_middleware(request: Request, call_next: Callable) -> Response:
    """
    在每个请求前创建一个数据库会话，并将其存储在request对象中的状态(state)中
    当请求处理完成后，会话将被关闭
    """
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionFactory()
        response = await call_next(request)
    finally:
        request.state.db.close()

    return response


def init_middleware(app: FastAPI) -> None:
    """初始化中间件并将其添加到FastAPI应用程序中，它将db_session_middleware注册为HTTP中间件
    """
    app.middleware("http")(db_session_middleware)
