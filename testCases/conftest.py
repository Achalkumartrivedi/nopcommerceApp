import pytest
import chromedriver_autoinstaller
from selenium import webdriver
import selenium
#from webdriver_manager.chrome import ChromeDriverManager



#@pytest.fixture(scope='session')
#def path_to_chrome():
#    return ChromeDriverManager().install()

@pytest.fixture
def chrome_driver_init():
     driver = chromedriver_autoinstaller.install()
     driver = webdriver.Chrome()
     return driver

#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

#import chromedriver_autoinstaller
#driver = chromedriver_autoinstaller.install()
#     driver = webdriver.Chrome()