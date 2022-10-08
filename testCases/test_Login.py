import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import chrome_driver_init
import chromedriver_autoinstaller
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGenclass
import datetime
import os


class Test_001_Login:
    baseurl = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password =  ReadConfig.getPassword()
    screenshotfolder = ReadConfig.getDirectory()
   #ss_login = ReadConfig.getTest1screenshot()
    #ss_loginpage = "../Screenshots/Login.png"
    #ss_dash = "..\\Screenshots\\" + "dashboard.png"


    logger = LogGenclass.loggenmethod() #call loggenmethod of LEggenClass



    def test_homePageTitle(self, chrome_driver_init):

        self.driver = chrome_driver_init
        self.logger.info("***** START Test 01: Login Page title verification *****")
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == 'Your store. Login':
            self.logger.info("***** Test 1 :Login page Title is Correct *****")
            print("\nTest 1: Login page title is correct\n")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(self.screenshotfolder+ '/Login.png')
            self.logger.info("***** Test 1 :Login page Title is Incorrect *****")
            print("LoginPage Title is incorrect")
            self.driver.close()
            assert False


    def Test_Login(self, chrome_driver_init):

        self.logger.info("Test_001_Home Page Title Verified")
        self.driver = chrome_driver_init
        self.driver.get(self.baseurl)
        print("\nTest 2: Login and Dashboard title is compared\n")
        self.lp = Login(self.driver)  #create of 'Login' class object
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            print( "Home Page Title is as expected")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.screenshotfolder+ '/Dashboard.png')
            print("HomePage Title is not as expected")
            self.driver.close()
            assert False





""""
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
