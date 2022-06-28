import os
from configparser import ConfigParser


_configparser = ConfigParser()
_configparser.optionxform = str


class Configurator:

    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self._parse_env()
        self._parse_config()

    def __getattr__(self, key):
        return self.__dict__.get(key)

    def _parse_env(self):
        env_file = os.path.join(self.BASE_DIR, os.environ['env_file'])
        _configparser.read(env_file)
        for _, block in _configparser.items():
            for key, value in block.items():
                setattr(self, key, value)

    def _parse_config(self):
        with open(os.path.join(self.BASE_DIR, 'config.cfg')) as cfg:
            _configparser.read_string('[cfg]\n' + cfg.read())

        for key, value in _configparser.items('cfg'):
            setattr(self, key, value)


configurator = Configurator()
