"""
module to handle app level logging.

wrapper around stdlib logging module to apply configuration
"""
import logging
from logging import config
from sampleapp import config as appconfig


def get_logger(name: str) -> logging.Logger:
    """Return the logger object with loaded configuration."""
    cfg = appconfig.Config()
    if cfg.log():
        config.dictConfig(cfg.log())
    return logging.getLogger(name)
