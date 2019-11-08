# -*- coding: utf-8 -*-
import os
import time


def getNowTimestamp():
    """获取当前时间戳"""
    return time.time()


def decMakeDir(func):
    """根据判断是否生成文件"""
    print('1111')

    def handleFunc(*args, **kwargs):
        dirname = func(*args, **kwargs)
        print(dirname)
        if not os.path.exists(dirname):
            print('create file')
            os.makedirs(dirname)
        elif not os.path.isdir(dirname):
            print('not file')
            pass

        return dirname

    return handleFunc


def getWorkDir():
    """获取项目路径"""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@decMakeDir
def getTmpDir():
    """获取临时文件夹路径"""
    return os.path.join(getWorkDir(), "tmp")


@decMakeDir
def getLogDir():
    """获取日志文件夹路径"""
    return os.path.join(getTmpDir(), "log")


if __name__ == '__main__':
    print(getLogDir())
