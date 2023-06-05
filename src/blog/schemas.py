"""
对象模型定义
"""
from datetime import datetime
from typing import Optional, TypeVar

from pydantic import BaseModel, constr

from blog.models import BaseModel as DBModel

# TypeVar 可以用来定义一个抽象的类型参数，它表示一组类型之一，用于创建类型变量
# ModelType 用于限定继承于 DBModel 的模型类
ModelType = TypeVar("ModelType", bound=DBModel)
# CreateSchema 和 UpdateSchema 分别用于限定基于 BaseModel 的用于创建和更新记录的数据模型类
CreateSchema = TypeVar("CreateSchema", bound=BaseModel)
UpdateSchema = TypeVar("UpdateSchema", bound=BaseModel)


class InDBMixin(BaseModel):
    """ 基础模型
    它包含一个 id 属性，表示文章在数据库中的唯一标识符
    """
    id: int

    # 表示该模型可以与 ORM 框架进行交互
    class Config:
        orm_mode = True


class BaseArticle(BaseModel):
    """
    定义了 API 中使用的文章属性，包括 title 和 body 两个必需属性。
    title 最大长度为 500 个字符
    Optional[str] 表示 body 属性是可选的
    """
    title: constr(max_length=500)
    body: Optional[str] = None


class ArticleSchema(BaseArticle, InDBMixin):
    """
    继承了 BaseArticle 和 InDBMixin 模型
    并添加了 create_time 和 update_time 两个时间戳属性
    这个模型可以用于从数据库中检索文章数据。
    """
    create_time: datetime
    update_time: datetime


class CreateArticleSchema(BaseArticle):
    """
    继承了 BaseArticle ，但不包含其他属性
    这个模型用于创建新文章时将标题和正文发送到 API
    """
    pass


class UpdateArticleSchema(BaseArticle):
    """
    继承了 BaseArticle ，但 title 属性变成了可选项
    这个模型用于客户端更新现有文章并仅发送要更改的属性，而不是整个文章对象
    """
    title: Optional[constr(max_length=500)] = None
