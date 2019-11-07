import os
import time
import logging
from logging import StreamHandler
from logging import FileHandler
from scripts.core import sys_util


# 直接继承logging.Logger 那么就是说这个类就是一个Logger， 有了Logger所有方法
# 只是在类里面添加一些内部方法，让logger 封装addhandler, setformatter等方法
class LogHandler(logging.Logger):
    # 单例模式
    _instance = None
    _suffix = ''  # 除了日期外的后缀

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            # 一开始居然用了 cls()来实例化 导致无限次调用
            # cls._instance = cls(*args, **kwargs)
            cls._instance = object.__new__(cls)
        return cls._instance

    def __init__(self, name, level=logging.DEBUG, to_stream=True,
                 to_file=True):
        self.name = name
        self.level = level
        self.formatter = logging.Formatter(
            '[crawler] %(asctime)s %(levelname)s [%(thread)d] %(name)s | %(message)s',
            '%Y-%m-%d %H:%M:%S'
        )
        # 错误的， 继承了logger 本身就是logger 不用再self.logger=xxx 这样变成了一个新的变量
        # self.logger = logging.Logger(name=name, level=level)
        super(LogHandler, self).__init__(name=name, level=level)

        # 写文件
        if to_file:
            self.__setFileHandler__()

        # 写标准输出
        if to_stream:
            self.__setSteamHandler__()

    def getTodayDateStr(self):
        return time.strftime("%Y-%m-%d",
                             time.localtime(sys_util.getNowTimestamp()))

    def getLogFile(self):
        # 设置文件名称
        todayStr = self.getTodayDateStr()
        rtn = os.path.join(sys_util.getLogDir(), todayStr)
        if self._suffix:
            rtn += "_" + self._suffix
        return rtn + ".log"

    def __setSteamHandler__(self):
        stream_handler = StreamHandler()
        stream_handler.setFormatter(self.formatter)
        self.addHandler(stream_handler)

    def __setFileHandler__(self):
        # 获取日志文件路径
        log_path = self.getLogFile()
        handler = FileHandler(log_path, encoding='utf-8')
        handler.setFormatter(self.formatter)
        self.addHandler(handler)


if __name__ == '__main__':
    logger = LogHandler('scrapy')
    logger.info('haha')
