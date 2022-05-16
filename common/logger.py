#默认日志格式
DEFAULT_LOG_FMT='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'
#默认时间格式
DEFUALT_LOG_DATEFMT='%Y-%m-%d %H:%M:%S'
#输出日志路径
import os
LOG_OUT_PATH=os.path.dirname(os.path.dirname(__file__))+'/log/'
if not os.path.exists(LOG_OUT_PATH):
    # 目录不存在，进行创建操作
    os.makedirs(LOG_OUT_PATH) #使用os.makedirs()方法创建多层目录
import sys
import logging
from time import strftime

class Logger(object):
    def __init__(self):
        self._logger=logging.getLogger()
        self.DEFAULT_LOG_FILENAME='{0}{1}.log'.format(LOG_OUT_PATH,strftime("%Y-%m-%d"))
        self.formatter=logging.Formatter(fmt=DEFAULT_LOG_FMT,datefmt=DEFUALT_LOG_DATEFMT)
        self._logger.addHandler(self._get_file_handler(self.DEFAULT_LOG_FILENAME))
        self._logger.addHandler(self._get_console_handler())
        self._logger.setLevel(logging.INFO)

    def _get_file_handler(self,filename):
        filehandler=logging.FileHandler(filename,mode='a+',encoding='utf-8')
        filehandler.setFormatter(self.formatter)
        return filehandler

    def _get_console_handler(self):
        console_handler=logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler
    @property
    def logger(self):
        return self._logger

# if __name__ == '__main__':
#     import datetime
#     logging=Logger().logger
#     logging.info(u'{}:开始XXX操作'.format(datetime.datetime.now()))
