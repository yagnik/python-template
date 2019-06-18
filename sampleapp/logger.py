"""
module to handle app level logging.

wrapper around logging module
"""
import logging
from logging import config
import config as appconfig

def get_logger(name):
    cfg = appconfig.Config()
    if cfg.log():
        config.dictConfig(cfg.log())
    return logging.getLogger(name)
