import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
import chromedriver_autoinstaller
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGenclass
import datetime
import os
import time
from utilities import XLUtils
from openpyxl import load_workbook


class Test_001_Login_DDT:
    baseurl = ReadConfig.getBaseURL()
    path = r'C:\Users\achal\PycharmProjects\nopcommerceApp\Testdata\logintestdata.xlsx'
    logger = LogGenclass.loggenmethod() #call loggenmethod of LEggenClass


    def test_DashboardPage(self, setup):

        self.logger.info("***** START : DATA DRIVEN TESTING OF LOGIN  *****")
        self.logger.info("***** DDT Test : Login with Data Driven Sheet and Dashboard title is compared  *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        print("\n DDT Test : Login with Data Driven Sheet and Dashboard title is compared\n")

        self.row = XLUtils.getRowCount(self.path, 'sheet1')
        print("No. of rows in test sheet: ", self.row)
        self.column = XLUtils.getColumCount(self.path, 'sheet1')
        print("No. of Column in test sheet: ", self.column)

        lst_status = []

        for r in range(2, self.row + 1):
            self.user = XLUtils.readData(self.path, 'sheet1', r, 1)
            self.logger.info("*****    Read Username from sheet    *****")
            self.password = XLUtils.readData(self.path, 'sheet1', r, 2)
            self.logger.info("*****    Read Password from sheet    ******")
            self.exp = XLUtils.readData(self.path, 'sheet1', r, 3)
            self.logger.info("*****    Read Expected from sheet    ******")

            self.lp = Login(self.driver)
            self.lp.setUserName(self.user)
            print("username from Sheet is:", self.user)
            self.lp.setPassword(self.password)
            print("Password from Sheet is:", self.password)
            time.sleep(3)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if self.exp == "Pass":
                    self.logger.info("*****   PASS: Valid Login ,Dashboard title is correct, status is 'PASS'   ***** ")
                    self.lp.clickLogout()
                elif self.exp == "Fail":
                    self.logger.info("*****   FAIL: Valid Login ,Dashboard title is correct , status is 'FAIL'  ******")
                    self.lp.clickLogout()
            else:
                if self.exp == "Pass":
                    self.logger.info("******** PASS: Invalid Login , status is 'PASS' ****** ")
                elif self.exp == "Fail":
                    self.logger.info("***** FAIL: Invalid Login, status is 'FAIL'  ***** ")
                    self.driver.save_screenshot(ReadConfig.getDDTscreenshot() + '/Login_DDT.png')

        self.logger.info("*****    End of DDT Testing       *****")
        self.logger.info("*****    Completed Test_001_Login_DDT    *****")
        print("\nEnd of Data Driven Testing")
        self.driver.close()
        print("\nBrowser Closed !")







""""
Run One : pytest -s -v testCases/test_login.py --browser chrome 
Run parallel :pytest -v -n=2 testCases/test_login.py 
Run  :for HTML reports pytest -v -n=2 --html=Reports/report.html testCases/test_login.py --browser chrome 



ss_loginpage = "../Screenshots/Login.png"
ss_dash = "..\\Screenshots\\" + "dashboard.png"


- Sleep function use for hold execution on page for second that given in parameter
from time import sleep
sleep(2)


# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())


SCREENSHOT TIMESSTAMP FOLDER
path = "../Screenshots"
DateString = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
os.chdir(path)
NewFolder = 'Test_shots_' + DateString
os.makedirs(NewFolder)
driver.save_screenshot(NewFolder + '/Login.png')


"""
