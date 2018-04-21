# --coding:utf-8--
import logging.handlers


class Log:
    def __init__(self):
        self.log = None

        self.levels = {"n": logging.NOTSET,
                       "d": logging.DEBUG,
                       "i": logging.INFO,
                       "w": logging.WARN,
                       "e": logging.ERROR,
                       "c": logging.CRITICAL}

        self.log_level = "d"
        self.log_file = "data_debug.log"
        self.log_max_byte = 10 * 1024 * 1024
        self.log_backup_count = 5
        self.encoding = 'utf-8'

    def get_logger(self):
        if self.log is not None:
            return self.log

        self.log = logging.Logger("oggingmodule.Logger")
        log_handler = logging.handlers.RotatingFileHandler(filename=self.log_file,
                                                           maxBytes=self.log_max_byte,
                                                           backupCount=self.log_backup_count,
                                                           encoding=self.encoding)
        log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
        log_handler.setFormatter(log_fmt)
        self.log.addHandler(log_handler)
        self.log.setLevel(self.levels.get(self.log_level))
        return self.log

    def _log(self, m):
        self.log.setLevel(self.levels.get(m))
        Log().get_logger()

    @staticmethod
    def error(msg):
        logger = Log().get_logger()
        logger.log_file = "data_error.log"
        logger.error(msg)

    @staticmethod
    def debug(*msgs):
        logger = Log().get_logger()
        logger.log_file = "data_debug.log"
        message = 'yaowei----'
        for msg in msgs:
            msg = str(msg)
            message = message + msg + '  '

        print(message)
        logger.debug(message)



if __name__ == "__main__":
   Log.debug('3344', '我是中文')
