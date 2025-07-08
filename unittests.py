import logs

import json
import typing
import pathlib
import datetime
from time import sleep
import logging


# украдено отсюда: https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python
def validate_datetime(string: str) -> bool:
    try:
        datetime.datetime.fromisoformat(string)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
    return True

def logs_test() -> bool:
    print(".", end="")
    all_right: bool = True
    logs.setup_logging()
    logger = logging.getLogger("unittests")
    logger.debug("debug message", extra={"x": "hello"})
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1/0 # type: ignore
    except ZeroDivisionError:
        logger.exception("exception message")
    
    sleep(5)
    log_file = pathlib.Path("logs/druid.jsonl")
    with open(log_file) as f_in:
        log_lines = f_in.read()
        logs_list: typing.List[str] = [log for log in log_lines.splitlines()]
        data = json.loads(logs_list[0])

        all_right = data["level"] == "DEBUG" and data["message"] == "debug message" and validate_datetime(data["timestamp"]) and data["logger"] == "unittests" 
        data = json.loads(logs_list[1])
        all_right = all_right and data["level"] == "INFO" and data["message"] == "info message" and validate_datetime(data["timestamp"]) and data["logger"] == "unittests" 
        data = json.loads(logs_list[2])
        all_right = all_right and data["level"] == "WARNING" and data["message"] == "warning message" and validate_datetime(data["timestamp"]) and data["logger"] == "unittests" 
        data = json.loads(logs_list[3])
        all_right = all_right and data["level"] == "ERROR" and data["message"] == "error message" and validate_datetime(data["timestamp"]) and data["logger"] == "unittests" 
        data = json.loads(logs_list[4])
        all_right = all_right and data["level"] == "CRITICAL" and data["message"] == "critical message" and validate_datetime(data["timestamp"]) and data["logger"] == "unittests" 
        data = json.loads(logs_list[5])
        all_right = all_right and "1/0" in data["message"]

    return all_right


def run_tests():
    if not logs_test():
        print("Что-то не так с logs.py")
        logs.end_logging()
        exit()
    print("\nEnded testing, all is fine")