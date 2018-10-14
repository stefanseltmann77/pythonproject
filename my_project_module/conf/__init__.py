import configparser

from .config_default import default_config

config_oracle = configparser.ConfigParser()
config_oracle.read_dict(default_config)
