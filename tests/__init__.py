import os

from blog.config import settings

# 加载了两个测试配置，和 Dynaconf 规则一样， settings.local.yml 配置为本地配置，不会被代码追踪
settings.load_file(os.path.join(os.path.dirname(__file__), 'settings.yml'))
settings.load_file(os.path.join(os.path.dirname(__file__), 'settings.local.yml'))

