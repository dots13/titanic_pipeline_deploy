import logging
from classification_model.config.core import PACKAGE_ROOT, config
""""
# Setup detailed logging for development
logger = logging.getLogger(config.app_config.package_name)
logger.setLevel(logging.DEBUG)  # Use DEBUG level for detailed output

# Create a console handler to output logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Define a formatter and add it to the handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the console handler to the logger
logger.addHandler(console_handler)
"""

logging.getLogger(config.app_config.package_name).addHandler(logging.NullHandler())

with open(PACKAGE_ROOT / "VERSION") as version_file:
    __version__ = version_file.read().strip()

