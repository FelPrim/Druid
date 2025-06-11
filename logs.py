import logging
import logging.handlers

def my_logger(name: str, level = logging.DEBUG) -> logging.Logger: # type: ignore
    logger = logging.getLogger(name)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    file_handler = logging.handlers.RotatingFileHandler(
        'druid.log',
        maxBytes=50*1024*1024,
        backupCount=1
    )

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger

logging.basicConfig(
    filename='basic.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
