#!/usr/bin/env python3


"""
Modules to be imported for running this script
"""

import logging
from logging.handlers import RotatingFileHandler


def logger(csv_log_file_path, log_id):
    logger = logging.getLogger("DEXCOM_BLE_logger")
    if log_id == 1:
        logger.setLevel(logging.INFO)
    if log_id == 2:
        logger.setLevel(logging.WARNING)
    file_handler = RotatingFileHandler(csv_log_file_path, maxBytes=1000000, backupCount=10)
    if log_id == 1:
        file_handler.setLevel(logging.INFO)
    if log_id == 2:
        file_handler.setLevel(logging.WARNING)

    f_format = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(f_format)
    logger.addHandler(file_handler)
    return logger
