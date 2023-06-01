# from sqlalchemy import create_engine
#
# engine = create_engine(
#     "mysql+pymysql://root:root@192.168.1.222:3306/",
#     echo=True,  # 是否转化为 sql 语句打印
#     pool_size=8,  # 连接池大小，默认 5 个，0 表示无限制
#     pool_recycle=60 * 10,  # 设置自动断开时间
# )
#
# try:
#     conn = engine.connect()
#     print("数据库连接成功")
# except Exception as e:
#     print(f"数据库连接出错：{e}")
# finally:
#     conn.close()

__version__ = "0.1.0"

from blog.db import engine
from blog.models import BaseModel

# 首先创建表
BaseModel.metadata.create_all(bind=engine)
