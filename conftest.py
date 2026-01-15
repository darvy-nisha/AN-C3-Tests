import time
import pytest
from selenium import webdriver
@pytest.fixture()
def setup(request):

    request.cls.driver = webdriver.Chrome()
    request.cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(10)
    yield
    request.cls.driver.quit()