"""
创建服务启动逻辑
"""

import uvicorn
from fastapi import FastAPI

from src.blog import middlewares, routes
from src.blog.config import settings
from src.blog.log import init_log


class Server:
    def __init__(self):
        init_log()
        self.app = FastAPI()

    def init_app(self):
        middlewares.init_middleware(self.app)
        routes.init_routers(self.app)

    def run(self):
        self.init_app()
        uvicorn.run(
            app=self.app,
            host=settings.HOST,
            port=settings.PORT,
        )
