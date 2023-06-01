import os

from blog.utils import chdir


def test_chdir():
    path = '/tmp'
    cwd = os.getcwd()
    with chdir(path):
        assert path == os.getcwd()
    assert cwd == os.getcwd()