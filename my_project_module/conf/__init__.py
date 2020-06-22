import configparser
import os
from pathlib import Path

from .config_default import default_config

project_root = Path(os.path.abspath(__file__)).parents[2]

config_oracle = configparser.ConfigParser()
config_oracle.read_dict(default_config)
