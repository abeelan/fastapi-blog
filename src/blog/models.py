"""
数据模型 表 定义

创建一个基本的 Article 表
包含四个字段，分别是 id、title、body、create_time 和 update_time
"""

from datetime import datetime

# Column类用于定义列
# DateTime类用于定义日期时间类型
# Integer类用于定义整数类型
# String类用于定义字符串类型
# Text类也用于定义字符串类型，但与String不同的是，它可以存储更长的字符串
from sqlalchemy import Column, DateTime, Integer, String, Text
# declarative_base函数则用于创建模型基础类，declared_attr 装饰器用于动态定义属性
from sqlalchemy.ext.declarative import declarative_base, declared_attr


class CustomBase:
    """https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html"""

    @declared_attr
    def __tablename__(cls):
        """
        使用 @declared_attr 装饰器修饰 __tablename __类方法
        使得在每个继承 CustomBase 的子类中都会自动设置表名为该子类的类名（小写形式）
        :return:
        """
        return cls.__name__.lower()

    # 定义通用表参数，以便复用
    # mysql_engine  表示 MySQL 数据库引擎
    # mysql_collate 表示字符集
    __table_args__ = {"mysql_engine": "InnoDB", "mysql_collate": "utf8mb4_general_ci"}

    # 自动创建 id，子类则不用再次声明该字段
    id = Column(Integer, primary_key=True, autoincrement=True)


# 从 CustomBase 类和 declarative_base 函数生成的模型基础类派生出来，从而获得其基本功能
BaseModel = declarative_base(cls=CustomBase)


class Article(BaseModel):
    """Article table"""

    title = Column(String(500))
    body = Column(Text(), nullable=True)
    create_time = Column(DateTime, default=datetime.now, nullable=False)
    update_time = Column(
        DateTime, default=datetime.now, onupdate=datetime.now, nullable=False
    )
