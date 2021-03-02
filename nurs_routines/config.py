"""
Config file for global parameters.
"""
import yaml

# Config.yaml definitions:
with open("config.yaml", "r") as f:
    CONFIG_DICT = yaml.safe_load(f)

EXTRACT_PATH = CONFIG_DICT.get("Extract Path")
ALLOCATE_WARD_COLUMN = CONFIG_DICT.get("AllocateWardColumn")
