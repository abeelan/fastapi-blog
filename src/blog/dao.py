"""
数据访问层
"""

from typing import Generic, List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from blog.models import Article
from blog.schemas import (CreateArticleSchema, CreateSchema, ModelType,
                      UpdateArticleSchema, UpdateSchema)


class BaseDAO(Generic[ModelType, CreateSchema, UpdateSchema]):
    """
    data access object
    定义了一个通用的数据访问对象（DAO）类 BaseDAO
    它是一个泛型类，可以为任何类型的模型提供通用的 CRUD 操作

    Generic 是一个泛型的抽象基类
    """
    model: ModelType

    def get(self, session: Session, offset=0, limit=10) -> List[ModelType]:
        """
        接收一个 SQLalchemy 的 session 对象，查询起始偏移量和查询结果数量限制
        使用给定参数从数据库中获取一组模型实例，并将其作为列表返回
        """
        result = session.query(self.model).offset(offset).limit(limit).all()
        return result

    def get_by_id(
        self,
        session: Session,
        pk: int,
    ) -> ModelType:
        """接收一个 session 对象和模型的主键，返回匹配的单个模型实例"""
        return session.query(self.model).get(pk)

    def create(self, session: Session, obj_in: CreateSchema) -> ModelType:
        """Create
        接收创建模式输入（即一个 Pydantic 模型），创建并提交一个新模型实例，并将其返回
        """
        obj = self.model(**jsonable_encoder(obj_in))
        session.add(obj)
        session.commit()
        return obj

    def patch(self, session: Session, pk: int, obj_in: UpdateSchema) -> ModelType:
        """Patch
        接收模型的主键和更新模式输入（即一个 Pydantic 模型），更新匹配的模型实例，并将其返回
        """
        obj = self.get_by_id(session, pk)
        update_data = obj_in.dict(exclude_unset=True)
        for key, val in update_data.items():
            setattr(obj, key, val)
        session.add(obj)
        session.commit()
        session.refresh(obj)
        return obj

    def delete(self, session: Session, pk: int) -> None:
        """Delete
        接收模型的主键，查找并删除匹配的模型实例
        """
        obj = self.get_by_id(session, pk)
        session.delete(obj)
        session.commit()

    def count(self, session: Session):
        """返回模型的总数（行数）"""
        return session.query(self.model).count()


class ArticleDAO(BaseDAO[Article, CreateArticleSchema, UpdateArticleSchema]):
    model = Article
