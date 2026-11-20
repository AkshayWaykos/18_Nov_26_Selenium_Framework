from datetime import datetime
import configparser

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


#Below Code with Config ini file      #Approch 1

    @staticmethod
    def getAppCred(key):
        config = configparser.RawConfigParser()  # create object of RawConfigParser class
        config.read(".\\ConfigurationFiles\\config.ini")  #
        value = config.get("App_Credentials", key)
        return value

    print("----------------------------------------------------------")

    # Below Code with Config ini file      #Approch 2

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
