"""
数据库连接 会话初始化
"""

from sqlalchemy.engine import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine.url import URL
from sqlalchemy.orm import scoped_session, sessionmaker

from blog.config import settings

url = URL(
    drivername=settings.DATABASE.DRIVER,
    username=settings.DATABASE.get("USERNAME", None),
    password=settings.DATABASE.get("PASSWORD", None),
    host=settings.DATABASE.get("HOST", None),
    port=settings.DATABASE.get("PORT", None),
    database=settings.DATABASE.get("NAME", None),
    query=settings.DATABASE.get("QUERY", None),
)

# echo 是否打印转化后的 sql 语句
engine: Engine = create_engine(url, echo=True)

# 为每个线程创建一个 Session 实例，并使用提供的引擎将其连接到数据库
# autocommit autoflush 分别指示事务自动提交和自动刷新
SessionFactory = sessionmaker(bind=engine, autocommit=False, autoflush=True)

# 创建了一个作用域会话类，它返回当前线程的单个会话
ScopedSession = scoped_session(SessionFactory)
