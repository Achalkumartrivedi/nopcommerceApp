import pytest
from selenium import webdriver
from demoPackage.fixuredemo.fixureClass import chrome_driver_init

def test_1(chrome_driver_init):
    pass


def test_2(chrome_driver_init):
    pass

# 1) chrome auto installer
# import chromedriver_autoinstaller
# driver = chromedriver_autoinstaller.install()
# driver = webdriver.Chrome()

# 2) chrome webdriver manager
# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(ChromeDriverManager().install())

# 3)fixture scope session
# set-> if fixtures in different class-> from testCases.conftest import path_to_chrome
# @pytest.fixture(scope='session')
# def path_to_chrome():
#   return ChromeDriverManager().install()

# driver = webdriver.Chrome(executable_path=path_to_chrome) //write in different function

# 4) Fixures code
# fixture class
# from webdriver_manager.chrome import ChromeDriverManager
# @pytest.fixture
# def chrome_driver_init():
#    driver = webdriver.Chrome(ChromeDriverManager().install())
#   driver.get('https://google.com')
#    driver.maximize_window()
#    yield
#    driver.quit()

# TestClass
# from demoPackage.fixureClass import chrome_driver_init
#def test_1(chrome_driver_init):
#    pass
# def test_2(chrome_driver_init):
#    pass