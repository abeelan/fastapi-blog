from logging.config import dictConfig

from blog.config import settings


def init_log():
    log_config = {
        # 指定配置文件的版本
        "version": 1,
        # 是否禁用已经存在的 logger 实例，默认为 False，表示不禁用
        "disable_existing_loggers": False,
        # 日志格式化字典，包含了三个格式化方式
        "formatters": {
            # 简单日志格式化器，将日志信息按照时间、级别和消息的顺序展示
            "sample": {"format": "%(asctime)s %(levelname)s %(message)s"},
            # 详细日志格式化器，将日志信息按照时间、级别、名称、进程 ID、线程 ID 和消息的顺序展示
            "verbose": {
                "format": "%(asctime)s %(levelname)s %(name)s %(process)d %(thread)d %(message)s"
            },
            # 访问日志格式化器，使用自定义的 AccessFormatter 类来格式化日志
            "access": {
                "()": "uvicorn.logging.AccessFormatter",
                "fmt": '%(asctime)s %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s',
            },
        },
        # console 的控制台处理程序 使用 verbose 格式化器进行日志格式化，并将日志级别设置为 DEBUG
        "handlers": {
            "console": {
                "formatter": "verbose",
                "level": "DEBUG",
                "class": "logging.StreamHandler",
            },
        },
        # logger 字典，包含了一个空字符串键值对，表示根 logger 实例
        # 该 logger 的日志级别被设置为 settings.LOG_LEVEL（从配置文件中获取），并且使用 console 处理程序来处理日志信息
        "loggers": {
            "": {"level": settings.LOG_LEVEL, "handlers": ["console"]},
        },
    }

    # 调用 dictConfig 方法并传入 log_config 参数以完成日志配置初始化
    dictConfig(log_config)
