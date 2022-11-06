import pytest
import chromedriver_autoinstaller
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service #impor service for 'service=Service(ChromeDriverManager().install())'
# Firefox
from webdriver_manager.firefox import GeckoDriverManager
# Edge
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService



@pytest.fixture
def setup(browser):
   if browser == 'edge':
      driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
      print("Edge Browser is Launching.....")
   elif browser == 'firefox':
      driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
      print("Firefox Browser is Launching.....")
   else:
      driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
      print("Chrome Browser is Launching.....")
   return driver

#without 'service=Service' gives warning in terminal:- "DeprecationWarning: executable_path"

def pytest_addoption(parser):
   parser.addoption("--browser") # This will get the value from CLI/hooks


@pytest.fixture
def browser(request):  # This will return the broswer value to setup method
   return request.config.getoption("--browser")


######## pytest HTML report ##########

# It is hook for adding environment info to HTML report
def pytest_configure(config):
   config._metadata['Project Name'] = 'nop Commerece'
   config._metadata['Module Name'] = 'Customer'
   config._metadata['Tester Name'] = 'Achal'

#It is hook for Delete/modify Environment info for HTML report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
   metadata.pop("JAVA_HOME", None)
   metadata.pop("Plugins", None)







#@pytest.fixture
#def setup():
#     driver = chromedriver_autoinstaller.install()
#     driver = webdriver.Chrome()
#     return driver

#@pytest.fixture(scope='session')
#def path_to_chrome():
#return ChromeDriverManager().install()


#from webdriver_manager.chrome import ChromeDriverManager
#driver = webdriver.Chrome(ChromeDriverManager().install())

#import chromedriver_autoinstaller
#driver = chromedriver_autoinstaller.install()
#     driver = webdriver.Chrome()