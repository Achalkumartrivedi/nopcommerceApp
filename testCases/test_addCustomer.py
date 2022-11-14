import random
import string

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
from selenium.webdriver.common.by import By


class Test_003_AddnewCustomer:
    baseurl = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password =  ReadConfig.getPassword()
    #screenshotfolder = ReadConfig.getDirectory() for common folder

    logger = LogGenclass.loggenmethod() #call loggenmethod of LEggenClass

    def test_AddNewCustomer(self, setup):

        self.logger.info("*****  Start Test03 : Add New Customer  *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        print("Start Test03 : Add New Customer\n")

        self.lp = Login(self.driver)  #create of 'Login' class object
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*****   Login successful   *****")
        time.sleep(3)

        self.logger.info("*****   Going to Add New Customer form  *****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()

        self.addcust.clickOnAddnew()

        self.logger.info("*****    Starting customer form filling   *****")

        self.email = random_generator() + "@yopmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstname("Alexander")
        self.addcust.setLastame("George")
        self.addcust.clickOnGender("Male") #Male select
        self.addcust.setDob("2/13/2000") # Format: D/M/Y
        self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerOfVender("Vendor 2")
        self.addcust.setAdmincomment("Admin comment is here")
        self.addcust.clickOnSavebtn()

        self.logger.info("*****   Saving customer info   *****")

        self.logger.info("*****   successful message verification started   *****")

        self.msg = self.driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissable").text

        print("Validation message is:",self.msg)
        if 'The new customer has been added successfully' in self.msg:
            assert True == True
            self.logger.info("*****   Add Customer Test Passed    *****")
            print("Add Customer Test Passed\n")
        else:
            self.driver.save_screenshot("../Screenshots"+"test_addCustomer_scr.png")
            self.logger.error("*****   Add Customer Test Failed    *****")
            assert True == False
            print("Add Customer Test Failed\n")

        self.driver.close()
        self.logger.info("*****    ENDING of Test 03:Add New Customer    *****")
        print("********  Program Run successfully ,ending of Add New Customer Test ******\n")


def random_generator(size=8,chars=string.ascii_lowercase+ string.digits):
    return ''.join(random.choice(chars) for x in range(size))