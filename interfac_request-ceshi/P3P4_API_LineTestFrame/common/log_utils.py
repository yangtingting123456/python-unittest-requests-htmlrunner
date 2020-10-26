#!/usr/bin/env python
# encoding: gbk
# @author: liusir
# @file: log_utils.py
# @time: 2020/10/18 10:46 ����

import os
import logging
from logging import handlers
from common.config_utils import config

log_path = os.path.join( os.path.dirname(__file__),'..', config.LOG_PATH )

class LogUtils:
    def __init__(self,log_path = log_path ):
        self.log_file_name = 'API_TEST_LOG.log'
        self.logger = logging.getLogger('API_TEST_LOG')
        self.logger.setLevel( config.LOG_LEVEL )

        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        console_handler.setLevel( config.LOG_LEVEL )

        file_handler = handlers.TimedRotatingFileHandler(os.path.join(log_path,self.log_file_name),when='D',interval=1,backupCount=7)
        file_handler.setLevel( config.LOG_LEVEL )
        file_handler.setFormatter( formatter )

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()  # ��ֹ��ӡ��־�ظ�
        file_handler.close()  # ��ֹ��ӡ��־�ظ�

    def get_logger(self):
        return self.logger

logger = LogUtils().get_logger()

if __name__=='__main__':
    logger.debug('newdream')