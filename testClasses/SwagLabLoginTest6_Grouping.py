import time
import pytest
from selenium import webdriver

from pageClasses.Home import SwagLabHomePage
from pageClasses.Login import SwagLabLoginPage
from utilityClasses.UtilityFile import CommonFunction


class Test_SwagLabLogin:

    logger=CommonFunction.loggen()
    @pytest.mark.sanity
    def test_TC1_loginWithValidData(self,openBrowser,request):
        driver=openBrowser

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("username"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("password"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---clicked on login button---")
        time.sleep(3)

        homeObj = SwagLabHomePage(driver)
        actLogoText = homeObj.getLogoText()
        expLogoText = "Swag Labs"

        if actLogoText == expLogoText:
            self.logger.info("---Login Test is Passed---")
            assert True
        else:
            self.logger.info("---Login Test is Failed---")
            CommonFunction.captureSS(driver,request.node.name)
            assert False

        time.sleep(2)
        driver.quit()

    @pytest.mark.regression
    def test_TC2_loginWithInvalidData(self,openBrowser,request):
        driver=openBrowser

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("invalidPassword"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---Clicked o login button---")
        time.sleep(3)
        actLoginFailedErrorMsg = loginObj.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message match---")
            assert True
        else:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message mis-match---")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        time.sleep(3)
        driver.quit()

    @pytest.mark.smoke
    def test_TC3_loginWithInvalidData(self,openBrowser,request):
        driver=openBrowser

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("invalidPassword"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---Clicked o login button---")
        time.sleep(3)
        actLoginFailedErrorMsg = loginObj.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message match---")
            assert True
        else:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message mis-match---")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        time.sleep(3)
        driver.quit()

    @pytest.mark.functional
    def test_TC4_loginWithValidData(self,openBrowser,request):
        driver=openBrowser

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("username"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("password"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---clicked on login button---")
        time.sleep(3)

        homeObj = SwagLabHomePage(driver)
        actLogoText = homeObj.getLogoText()
        expLogoText = "Swag Labs"

        if actLogoText == expLogoText:
            self.logger.info("---Login Test is Passed---")
            assert True
        else:
            self.logger.info("---Login Test is Failed---")
            CommonFunction.captureSS(driver,request.node.name)
            assert False

        time.sleep(2)
        driver.quit()

    @pytest.mark.sanity
    @pytest.mark.functional
    def test_TC5_loginWithInvalidData(self,openBrowser,request):
        driver=openBrowser

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("invalidPassword"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---Clicked o login button---")
        time.sleep(3)
        actLoginFailedErrorMsg = loginObj.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message match---")
            assert True
        else:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message mis-match---")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        time.sleep(3)
        driver.quit()

    @pytest.mark.regression
    def test_TC6_loginWithInvalidData(self,openBrowser,request):
        driver=openBrowser

        loginObj = SwagLabLoginPage(driver)
        loginObj.enterUserName(CommonFunction.getAppCred("invalidUsername"))
        self.logger.info("---Username Entered---")
        time.sleep(2)
        loginObj.enterPassword(CommonFunction.getAppCred("invalidPassword"))
        self.logger.info("---Password Entered---")
        time.sleep(3)
        loginObj.clickOnLoginBtn()
        self.logger.info("---Clicked o login button---")
        time.sleep(3)
        actLoginFailedErrorMsg = loginObj.getLoginFailedErrorMsg()
        expLoginFailedErrorMsg = "Epic sadface: Username and password do not match any user in this service"

        if actLoginFailedErrorMsg == expLoginFailedErrorMsg:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message match---")
            assert True
        else:
            self.logger.info("---Login Failed Test is Passed: Act & Exp login failed error message mis-match---")
            CommonFunction.captureSS(driver, request.node.name)
            assert False

        time.sleep(3)
        driver.quit()




# Add parameter:     -n noOfWorkers
# pytest -v -s Test_Cases/SwagLoginTest.py --browser="edge" -n 2
