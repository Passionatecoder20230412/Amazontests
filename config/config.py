import datetime
import os


class Config:
    # project paths
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    LOG_DIR = os.path.join(BASE_DIR,'logs')
    REPORTS_DIR= os.path.join(BASE_DIR,'reports')
    SCREENSHOTS_DIR=os.path.join(BASE_DIR,'screenshots')

    #Test URLs
    BASE_URL="http://automationexcercise.com/"

    #Browser configurations
    BROWSER="chrome"
    HEADLESS=True
    IMPLICIT_WAIT=30
    EXPLICIT_WAIT=30

    #Test Data
    TEST_DATA_PATH=os.path.join(BASE_DIR,'test_data')

    #Logging configurations

    LOG_LEVEL="INFO"
    LOG_FORMAT="%(asctime)s - %(name)s - %(levelname)s - %(message)s"

    @staticmethod
    def get_timestamp():
        return datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

    @classmethod
    def setup_directories(cls):
        directories=[cls.LOG_DIR,cls.REPORTS_DIR,cls.SCREENSHOTS_DIR]
        for directory in directories:
            os.makedirs(directory, exist_ok=True)