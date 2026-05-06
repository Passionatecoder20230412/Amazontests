import logging
import os
from logging.handlers import RotatingFileHandler

from config.config import Config



class TestLogger:
    def __init__(self,name="TestFramework"):
        self.logger=logging.getLogger(name)
        self.logger.setLevel(getattr(logging,Config.LOG_LEVEL))

        #create logs directory if doesnt exist
        Config.setup_directories()

        #Formatter
        formatter=logging.Formatter(Config.LOG_FORMAT)

        #file handler
        log_file=os.path.join(Config.LOG_DIR,f"test_execution_{Config.get_timestamp()}.log")
        file_handler=RotatingFileHandler(
            log_file,maxBytes=10*1024*1024,backupCount=5)
        file_handler.setFormatter(formatter)

        #console handler
        console_handler=logging.StreamHandler()
        console_handler.setFormatter(formatter)

        #add handlers if not already added
        if not self.logger.handlers:
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def get_logger(self):
        return self.logger

    @staticmethod
    def log_step(step_description):
        def decorator(func):
            def wrapper(*args, **kwargs):
                logger=TestLogger().get_logger()
                logger.info(f"START STEP : {step_description}")
                try:
                    result = func(*args, **kwargs)
                    logger.info(f"END STEP : {step_description} - PASSED")
                    return result
                except Exception as e:
                    logger.error(f"END STEP : {step_description} - FAILED")
                    logger.error(f"Error: {str(e)}")
                    raise
            return wrapper
        return decorator

#singleton logger instance
logger=TestLogger().get_logger()