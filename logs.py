import logging
import logging.handlers
from env import DEBUG_LOG as IS_DEBUG
from typing import TypedDict

Log_dict = TypedDict("Log_dict",
                     {"handler": logging.handlers.RotatingFileHandler,
                         "formatter": logging.Formatter, "level": logging.NOTSET})


def generate_log_config() -> Log_dict:
    handler = logging.handlers.RotatingFileHandler(
        # all logs belong in a "logs" directory in the project's root directory
        filename='logs/discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotate through 5 files
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'  # year : month : day & hour : minute : second
    formatter = logging.Formatter(
        '[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    if IS_DEBUG:
        level = logging.DEBUG
    else:
        level = logging.WARNING
    return Log_dict(handler=handler, formatter=formatter, level=level)

    # return {"handler": handler,
    #         "formatter": formatter,
    #         "level": level
    #         }


log_config = generate_log_config()
