import logging
from datetime import datetime
import configparser
import openpyxl

class CommonFunction:

    #Author Name: Akshay
    # This method is used to capture the screenshot of the current page and save it in the Screenshots folder with the test name and current date & time.
    @staticmethod
    def captureSS(driver, test_name):
        # Current date & time
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Screenshot file name
        screenshot_path = f".\\Screenshots\\{test_name}_{current_time}.png"

        driver.save_screenshot(screenshot_path)

    @staticmethod
    def getAppCred(key):
        config = configparser.RawConfigParser()              # create object of RawConfigParser class
        config.read(".\\ConfigurationFiles\\config.ini")        #
        value = config.get("App_Credentials", key)
        return value

    @staticmethod
    def getAppURL():
        config = configparser.RawConfigParser()
        config.read(".\\ConfigurationFiles\\config.ini")        #
        value = config.get("App_Credentials", "URL")
        return value

    @staticmethod
    def getAppUN():
        config = configparser.RawConfigParser()
        config.read(".\\ConfigurationFiles\\config.ini")  #
        value = config.get("App_Credentials", "username")
        return value

    @staticmethod
    def getAppPWD():
        config = configparser.RawConfigParser()
        config.read(".\\ConfigurationFiles\\config.ini")  #
        value = config.get("App_Credentials", "password")
        return value

    @staticmethod
    def loggen():
        # Generate filename with current date & time -> convert to string
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = f".\\Logs\\SwagLabLogs_{current_time}.log"

        # The f stands for formatted string literal (also called an f-string)

        logging.basicConfig(filename=log_filename,
                format='%(asctime)s: %(levelname)s: %(message)s',
                datefmt="%Y-%m-%d %H:%M:%S",
                force=True)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

#Below Code is use to Take the data from Excel Sheet

    @staticmethod
    def getDataFromExcel(rowIndex,colIndex):
        workbook = openpyxl.load_workbook("C:\\Users\\Admin\\PycharmProjects\\PythonProject\\18_Nov_26_Selenium_Framework\\TestData\\SwagTestData.xlsx")
        sheet = workbook['TestData']

        cellValue = sheet.cell(rowIndex, colIndex).value
        return cellValue