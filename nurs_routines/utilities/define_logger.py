"""
Log information to file during routines.
"""

import sys
import os
import logging
import datetime

def define_logger(extract_path, file_name):
    """
    Alter logger settings for target path and file name.
    Prints logging.info and above to console.
    Adds logging.debug and above to file.
    Parameters
    ----------
    extract_path: str
        relative path to record log file at
    file_name: str
        name of log file (.log appended automatically)
    """
    file_path = os.path.join(extract_path, "extract_logs", file_name)
    log_file = file_path + ".log"

    logging.basicConfig(filename=log_file, level=logging.DEBUG)

    handler = logging.StreamHandler(sys.stdout)
    handler.setLevel(logging.INFO)

    logging.getLogger().addHandler(handler)
    logging.info("Logger open at %s", datetime.datetime.now())
    return logging.getLogger()
