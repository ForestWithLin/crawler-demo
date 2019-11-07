# -*- coding: utf-8 -*-
import os
import time


def getNowTimestamp():
    """获取当前时间戳"""
    return time.time()


def decMakeDir(func):
    """根据判断是否生成文件"""
    def handleFunc(*args, **kwargs):
        dirname = func(*args, **kwargs)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        elif not os.path.isdir(dirname):
            pass

        return dirname

    return func


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
