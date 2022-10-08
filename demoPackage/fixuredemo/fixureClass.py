import pytest
#import chromedriver_autoinstaller
from selenium import webdriver
import selenium
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def chrome_driver_init():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://google.com')
    driver.maximize_window()
    yield
    driver.quit()