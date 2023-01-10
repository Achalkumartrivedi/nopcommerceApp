import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from testCases.conftest import setup
import chromedriver_autoinstaller
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGenclass
import datetime
import os
import time
from utilities import XLUtils
from openpyxl import load_workbook

class Test_SearchCustomerByEmail_004:
    baseurl = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()
    email = ReadConfig.getEmail()
    logger = LogGenclass.loggenmethod()  # call loggenmethod of LEggenClass

    def test_searchCustomerByName(self,setup):
        self.logger.info("***** START: SearchCustomerByName_005 *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        print("***** START: SearchCustomerByName_005 *****")

        # Login pageobject from LoginPage.py
        self.lp = Login(self.driver)  # create of 'Login' class object
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("***** Login Successful  *****")
        print("***** Login Successful *****")

        self.logger.info("***** Starting Search Customer By Name *****")

        # Customer tabs pageobject from AddCustomerPage.py
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersSubMenu()

        #SearchByEmail pageobject from SearchCustomerPage.py
        self.searchcust = SearchCustomer(self.driver)
        self.searchcust.setFirstName("Victoria")  #self.email - direct pass value
        self.logger.info("***** Entered FirstName in field  *****")
        self.searchcust.clickSearch()
        self.logger.info("***** Click on Search button  *****")
        print("***** Click on Search button *****")
        time.sleep(5)
        status = self.searchcust.searchCustomerByName("Victoria Terces")
        print(status)

        if status == True:
            assert True == status
            print("***** Flag:True - Searched name is present in table *****")
            self.logger.info("***** ***** Flag:True - TC PASS: Searched name is present in table *****  *****")
        else:
            assert False == status
            print("***** Flag:FALSE - Searched name is not present in table *****")
            self.logger.info("***** ***** Flag:False - TC FAIL: Searched name is not present in table *****  *****")


        self.logger.info("***** Finsished: SearchCustomerByName_005 run successfully *****")
        print("***** Finsished: SearchCustomerByName_005 run successfully *****")

        self.driver.close()