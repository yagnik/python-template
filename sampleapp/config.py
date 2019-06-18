"""
module to handle app level configurations stored in config folder.

yet another detail
"""
import json
import os


class Config(object):
    """
    Main Config class to handle loading config files.

    The class acts as the main interface for configuration of the app
    """

    LOG_CONFIG_FILE = "log.json"
    APP_CONFIG_FILE = "app.json"

    def __init__(self) -> None:
        """Construct Config class."""
        self.config_path = os.path.join(
            os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "config"
        )
        self.log_config_path = os.path.join(self.config_path, self.LOG_CONFIG_FILE)
        self.app_config_path = os.path.join(self.config_path, self.APP_CONFIG_FILE)
        self.log_config: dict = {}
        self.app_config: dict = {}

    def log(self) -> dict:
        """Return log configuration."""
        if not self.log_config:
            self.log_config = self._load(self.log_config_path)
        return self.log_config

    def app(self) -> dict:
        """Return app configuration."""
        if not self.app_config:
            self.app_config = self._load(self.app_config_path)
        return self.app_config

    def _load(self, path) -> dict:
        if os.path.exists(path):
            return json.load(open(path))
        else:
            return {}
