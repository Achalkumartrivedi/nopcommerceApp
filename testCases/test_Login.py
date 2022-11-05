import pytest
from selenium import webdriver
from pageObjects.LoginPage import Login
from testCases.conftest import setup
import chromedriver_autoinstaller
from utilities.readProperties import ReadConfig
from utilities.customeLogger import LogGenclass
import datetime
import os


class Test_001_Login:
    baseurl = ReadConfig.getBaseURL()
    username = ReadConfig.getUsername()
    password =  ReadConfig.getPassword()
    #screenshotfolder = ReadConfig.getDirectory() for common folder

    logger = LogGenclass.loggenmethod() #call loggenmethod of LEggenClass



    def test_homePageTitle(self, setup):

        self.driver = setup
        self.logger.info("***** START Test 01: Login Page title verification *****")
        self.driver.get(self.baseurl)
        act_title = self.driver.title

        if act_title == 'Your store. Login':
            self.logger.info("***** Test 01 PASS: Login page Title is Correct *****")
            print("\nTest 01: Login page title is correct\n")
            self.driver.close()
            assert True
        else:
            self.driver.save_screenshot(self.ReadConfig.getLoginscreenshot()+ '/Login.png')
            self.logger.info("***** Test 01 FAIL: Login page Title is Incorrect *****")
            print("LoginPage Title is incorrect")
            self.driver.close()
            assert False


    def test_DashboardPage(self, setup):

        self.logger.info("***** START Test 02: Dashboad Page title verification *****")
        self.driver = setup
        self.driver.get(self.baseurl)
        print("\nTest 02: Login and Dashboard title is compared\n")
        self.lp = Login(self.driver)  #create of 'Login' class object
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title

        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("***** Test 02 PASS: Dashboard Page title is expected *****")
            print( "Home Page Title is as expected")
            self.driver.close()
        else:
            self.driver.save_screenshot(self.ReadConfig.getDashboardscreenshot()+ '/Dashboard.png')
            print("Test 02 FAIL: Dashboard Title is not as expected")
            self.driver.close()
            assert False





""""
Run One : pytest -s -v testCases/test_Login.py --browser chrome 
Run parallel :pytest -v -n=2 testCases/test_Login.py 
Run  :for HTML reports pytest -v -n=2 --html=Reports/report.html testCases/test_Login.py --browser chrome 



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
