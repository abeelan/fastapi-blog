## 简介

本项目是一个基于 fastapi 异步 Web 框架搭建的博客系统，业务功能比较简单，但体现了从环境搭建到开发到测试发布的完整流程。

环境：
- 开发语言 python 3.10
- 虚拟环境工具 poetry（要求 Python 3.7+ [快速上手](https://python-poetry.org/docs/)）

## 项目编写记录

### 项目环境管理工具 - poetry
支持同时管理开发生产环境依赖，自动查找虚拟环境，生成依赖锁定文件等其他特性。
[参考链接](https://abeelan.github.io/tech/python/poetry-%E7%8E%AF%E5%A2%83%E7%AE%A1%E7%90%86/)
安装完成后，还需要切换 shell 到该环境下
```shell
$ poetry shell
```

### 命令行工具 click
```shell
# 直接使用：在 cmdline 文件下加上 main 入口
# 直接执行

# 命令行执行
$ python cmdline.py -V

# 打包后通过包执行
$ pip install -e .
$ python -m blog.cmdline -V
```

### 引入 alembic 做数据库迁移
将包添加到依赖并安装
```shell
$ poetry add alembic
```
初始化
```shell
$ alembic init migration
$ mv alembic.ini src/blog/migration
```
创建空白数据库迁移版本
```shell
$ python src/blog/cmdline.py migrate -- revision -m "init"
```
执行迁移
```shell
$ python src/blog/cmdline.py migrate -- upgrade head
```
创建第一个数据库迁移版本
```shell
$ python src/blog/cmdline.py migrate -- revision --autogenerate -m "init_table"
```
执行迁移
```shell
$ python src/blog/cmdline.py migrate -- upgrade head
```