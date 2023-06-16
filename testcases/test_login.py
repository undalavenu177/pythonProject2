import time

import pytest
from selenium import webdriver
from self import self

from pageobjects.login import login
from utilities.readproperties import ReadConfig
from  utilities.cusomlogger import LogGen

class Test_001_login:
    baseURL=ReadConfig.getappurl(self)
    username=ReadConfig.getusermail(self)
    password=ReadConfig.getpassword(self)

    logger=LogGen.loggen()

    def test_homepagetitle(self,Setup):
        self.logger.info("*******Test_001-Login*********")
        self.logger.info("**********verify home page title*******")
        self.driver=Setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        print(act_title)
        if act_title=="Log in to Facebook":
            print(True)
            self.driver.save_screenshot(".\\sreenshots\\" + "test_homepageTitle1.png")
            self.logger.info("*************home page test is passed*******")

        else:
            print(False)
            self.driver.save_screenshot(".\\sreenshots\\" + "test_homepageTitle1.png")
            self.logger.error("****************home page test is failured***********")
    def test_login(self,Setup):
        self.logger.info("****************verify login test***********")
        self.driver=Setup
        self.lp=login(self.driver)
        self.driver.get(self.baseURL)  #calling login by creation of objects
        self.lp.SetUsername(self.username)
        self.lp.Password(self.password)
        self.lp.Login(self)
    def test_title(self,Setup):
        self.driver = Setup
        time.sleep(3)
        act_title1=self.driver.title
        print(act_title1)
        if act_title1 == "Facebook":
            print(True)
            self.logger.info("****************login test is passed***********")
        else:
            self.driver.save_screenshot(".\\sreenshots\\"+"test_homepageTitle.png")
            self.logger.error("****************login test is failured***********")

            print(False)


