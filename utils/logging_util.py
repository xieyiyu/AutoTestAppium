import logging.config
import os

from utils.yaml_util import get_yaml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

logging_file = get_yaml(PATH("../yamls/config/log_config.yaml"))
logging.config.dictConfig(logging_file)

log = logging.getLogger("fileLogger")
