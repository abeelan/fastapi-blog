"""
命令行工具定义
"""

from pathlib import Path

import click
from alembic import config
from click import Context

import blog
from blog import utils
from blog.config import settings
from blog.server import Server


# 此装饰器将函数声明为一个 Click 命令组，如果用户没有指定任何子命令，则将调用 main 函数
# invoke_without_command=True: 允许用户执行不带子命令的主命令
@click.group(invoke_without_command=True)
# 此装饰器将当前 Click 上下文对象作为第一个参数传递给该函数
# 上下文对象是一种包含有关 CLI 环境的信息和状态的对象，其中包括选项、参数、输入和输出等。
# 在函数中，可以通过 ctx 参数访问上下文对象。
@click.pass_context
# 此装饰器定义了一个名为 --version 或 -V 的单个选项，其类型为布尔值（即是或否）默认情况下为 False。
# 如果用户设置了该选项，则会打印版本号并退出
@click.option(
    "-V", "--version", is_flag=True, help="Show version and exit."
)
def main(ctx, version):
    """我自动变为命令行的帮助信息。"""
    # 选项中的 --version 就是这里的 version 传参
    if version:
        # 当匹配到选项的参数后，则执行
        click.echo(blog.__version__)
    elif ctx.invoked_subcommand is None:
        # 当没有选项或者选项不匹配时，显示帮助信息，比如：blog  或者 blog aa
        click.echo(ctx.get_help())


@main.command()
@click.option(
    "-h", "--host", show_default=True, help=f"Host IP. Default: {settings.HOST}"
)
@click.option(
    "-p", "--port", show_default=True, type=int, help=f"Port. Default: {settings.PORT}"
)
@click.option("--level", help="Log level")
def server(host, port, level):
    """Start server."""
    kwargs = {
        "LOGLEVEL": level,
        "HOST": host,
        "PORT": port,
    }
    # 命令行调用方式为：
    # blog server -h 192.168.xxx.xxx -p 9999 --level info
    click.echo(f"[{level}] {host}:{port}")

    for name, value in kwargs.items():
        if value:
            settings.set(name, value)

    Server().run()


@main.command()
@click.pass_context
@click.option('-h', '--help', is_flag=True)
# 由于使用了 click 包装了 alembic 命令，在使用上会有点不同
# 默认应该使用 migrate -- 后加 alembic 的其他参数，否则多参数的情况下会无法识别。
@click.argument('args', nargs=-1)
def migrate(ctx: Context, help, args):
    """usage migrate -- arguments
    """
    with utils.chdir(Path(__file__).parent / 'migration'):
        argv = list(args)
        if help:
            argv.append('--help')
        config.main(prog=ctx.command_path, argv=argv)
