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

    @pytest.mark.regression
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
            self.driver.save_screenshot(ReadConfig.getLoginscreenshot()+ '/Login.png')
            self.logger.info("***** Test 01 FAIL: Login page Title is Incorrect *****")
            print("LoginPage Title is incorrect")
            self.driver.close()
            assert False


    @pytest.mark.sanity
    @pytest.mark.regression
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
            self.driver.save_screenshot(ReadConfig.getDashboardscreenshot()+ '/Dashboard.png')
            print("Test 02 FAIL: Dashboard Title is not as expected")
            self.driver.close()
            assert False





""""
RUN BY TERMINAL : 
Run One : pytest -s -v testCases/test_login.py --browser chrome 
Run parallel :pytest -v -n=2 testCases/test_login.py 
Run  :for HTML reports pytest -v -n=2 --html=Reports/report.html testCases/test_login.py --browser chrome 
Run sanity after marking:  pytest -s -v -m "sanity" 
Run mehods which have both sanity and regresstion (only 1 executed): pytest -s -v -m "sanity and regression"
Run methods which have one of them (all exexuted): pytest -s -v -m "sanity or regression"
Run sanity with generate html code: pytest -v -m "sanity" --html=./Reports/report.html testCases/ --browser chrome

Make Run.bat file 
1)open project folder 2)create text file and rename run.bat
3)copy "pytest -v -m ......" in text file ,also use 'rem' for comment line
4)run bat file to click on it ,it run through command prompt



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
