import os
import sys
from pathlib import Path

from dynaconf import Dynaconf

# 指定根目录
_BASE_DIR = Path(__file__).parent.parent

# 指定绝对路径 加载默认配置
settings_files = [
    Path(__file__).parent / 'settings.yml',
]

settings = Dynaconf(
    envvar_prefix="BLOG",  # 环境变量前缀。设置`BLOG_FOO='bar'`，使用`settings.FOO`
    settings_files=settings_files,
    environments=False,  # 启用多层次日志，支持 dev, pro
    load_dotenv=True,  # 加载 .env
    env_switcher="BLOG_ENV",  # 用于切换模式的环境变量名称 BLOG_ENV=production
    lowercase_read=False,  # 禁用小写访问， settings.name 是不允许的
    includes=[os.path.join(sys.prefix, 'etc', 'blog', 'settings.yml')],  # 自定义配置覆盖默认配置
    base_dir=_BASE_DIR,  # 编码传入配置
)
