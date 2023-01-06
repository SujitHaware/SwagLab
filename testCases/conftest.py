import pytest
from selenium import webdriver

@pytest.fixture()
def setup(Browser = 'CHROME'):
    if Browser == 'CHROME':
        driver = webdriver.Chrome()
    elif Browser == 'EDGED':
        driver = webdriver.Edge()
    elif Browser == 'FIREFOX':
        driver = webdriver.Firefox()
    else:
        print('Invalid Browser Selection')
    return driver

