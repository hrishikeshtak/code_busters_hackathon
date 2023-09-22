import logging
import os
from typing import Union


class Helper:
    _level: Union[str, int] = os.environ.get("LOG_LEVEL", "INFO")
    if os.environ.get("LOG_LEVEL") in ("DEBUG", "INFO", "WARNING", "ERROR"):
        _level = os.environ["LOG_LEVEL"]

    logger = logging.getLogger()
    logger.setLevel(_level)

    handler = logging.StreamHandler()
    handler.setLevel(_level)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(threadName)s - %(name)s - %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    @classmethod
    def print_message(cls, *messages, level="info"):
        final_message = ""
        for message in messages:
            final_message = final_message + str(message) + " "

        if os.environ.get("ENV") == "local":
            log_message = final_message
        else:
            log_message = final_message.rstrip(" ")

        if level == "error":
            cls.logger.error(log_message)
        else:
            cls.logger.info(log_message)
