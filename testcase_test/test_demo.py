# -*- coding: UTF-8 -*-
import pytest


def setup_module():
    print('\n在执行测试用例之前初始化的代码')


def teardown_module():
    print('\n清理资源')


def test_01_login():
    print('\n登录')


def test_02_browse():
    print('\n浏览网页')


def test_03_exit():
    print('\n退出')


if __name__ == '__main__':
    pytest.main("['q'],test_module.py")
