import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    maximize_window(driver)
    request.cls.driver = driver
    yield
    driver.quit()


def maximize_window(driver):
    """
    Maximizes the browser window
    """
    driver.maximize_window()

