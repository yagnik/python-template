import pytest
import os
from unittest.mock import patch
from sampleapp import config


@pytest.fixture
def config_path():
    return os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config")


def test_config_constructor_sets_paths(config_path):
    cfg = config.Config()
    assert cfg.config_path == config_path, "root config path is not the same"
    assert cfg.log_config_path == os.path.join(cfg.config_path, cfg.LOG_CONFIG_FILE)
    assert cfg.app_config_path == os.path.join(cfg.config_path, cfg.APP_CONFIG_FILE)


def test_load_log_if_file_present():
    cfg = config.Config()
    assert len(cfg.log()) != 0


@patch("os.path.exists", lambda _: False)
def test_load_empty_log_if_file_not_present():
    cfg = config.Config()
    assert len(cfg.log()) == 0


def test_load_app_if_file_present():
    cfg = config.Config()
    assert len(cfg.app()) != 0


@patch("os.path.exists", lambda _: False)
def test_load_empty_app_if_file_not_present():
    cfg = config.Config()
    assert len(cfg.app()) == 0
