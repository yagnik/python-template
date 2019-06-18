from unittest.mock import patch
from sampleapp import logger


def test_get_logger_does_not_apply_config():
    with patch("sampleapp.config.Config.log", return_value={}):
        assert logger.get_logger("bar").getEffectiveLevel() == 30


def test_get_logger_applies_config():
    assert logger.get_logger("foo").getEffectiveLevel() == 10
