"""Module Level Logging"""
import logging
from datetime import datetime
from os import path


class UnixFormatter(logging.Formatter):
    """Formatter with Unix Timestamping"""
    def formatTime(self, record, datefmt=None):
        """Generates a Unix-style Timestamp"""
        time_struct = self.converter(record.created)
        return str(datetime(*time_struct[:6]).timestamp())


def get_logger():
    """Creates Result logger and Error logger"""
    fmt = UnixFormatter("%(asctime)s %(message)s")
    print(__file__)
    dirpath = path.abspath(path.join(__file__, "../../../output_dir"))
    result_logger = logging.getLogger("result")
    result_logger.setLevel(0)
    result_handler = logging.FileHandler(path.join(dirpath, "results.log"))
    result_handler.setLevel(logging.INFO)
    result_handler.formatter = fmt
    result_logger.addHandler(result_handler)
    result_logger.propagate = False
    error_logger = logging.getLogger("error")
    error_logger.setLevel(0)
    error_handler = logging.getLogger(path.join(dirpath, "error.log"))
    error_handler.setLevel(logging.ERROR)
    error_handler.formatter = UnixFormatter("%(message)s")
    error_logger.addHandler(error_handler)
    error_logger.propagate = False
    return result_logger, error_logger
