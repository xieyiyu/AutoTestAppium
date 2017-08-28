import logging.config
import os

from utils.yaml_util import get_yaml

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

logging_file = get_yaml(PATH("../yamls/config/log_config.yaml"))

info_log = logging_file['handlers']['info_file_handler']['filename']
error_log = logging_file['handlers']['error_file_handler']['filename']
logging_file['handlers']['info_file_handler']['filename'] = PATH("../log/%s" %info_log)
logging_file['handlers']['error_file_handler']['filename'] = PATH("../log/%s" %error_log)

logging.config.dictConfig(logging_file)

log = logging.getLogger("fileLogger")

# if __name__ == "__main__":
#     log.info(logging_file)
#     print(logging_file['handlers']['info_file_handler']['filename'])
#     info_log = logging_file['handlers']['info_file_handler']['filename']
#     error_log = logging_file['handlers']['error_file_handler']['filename']
#     logging_file['handlers']['info_file_handler']['filename'] = PATH("../log/%s" %info_log)
#     logging_file['handlers']['error_file_handler']['filename'] = PATH("../log/%s" %error_log)
#     print(logging_file['handlers'])
