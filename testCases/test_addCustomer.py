import pytest
from selenium import webdriver
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Login
from testCases.conftest import setup
import chromedriver_autoinstaller
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGenclass
import datetime
import os
import time


class Test_003_AddnewCustomer:
    baseurl = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password =  ReadConfig.getPassword()
    email = "abc@yopmail.com"
    cus_password = "123456"
    #screenshotfolder = ReadConfig.getDirectory() for common folder

    logger = LogGenclass.loggenmethod() #call loggenmethod of LEggenClass

    def test_AddNewCustomer(self, setup):

        self.logger.info("***** Test03 : Add New Customer *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        print("\n****  Test03 : Add New Customer  ****\n")

        self.lp = Login(self.driver)  #create of 'Login' class object
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login successful *****")
        time.sleep(3)
        self.logger.info("***** Starting Add customer test *****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()
        self.addcust.clickOnAddnew()

        self.logger.info("***** Starting Add customer test *****")
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Achalkumar")
        self.addcust.setLastame("Trivedi")
        self.addcust.clickOnMaleGender() #Male select
        self.addcust.setDob("2/13/2000") # Format: D/M/Y
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVender("Vendor 2")
        self.addcust.setAdmincomment("Admin comment is here")

        # self.addcust.clickOnSavebtn()
        self.logger.info("***** Success till now *****")
        print("***Program run success till now ***\n")


