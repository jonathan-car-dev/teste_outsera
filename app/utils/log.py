import logging

def print_log(msg, level=logging.INFO) -> None:
    logger = logging.getLogger('uvicorn')
    logger.log(level=level, msg=msg)
