import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def setup(request):
    """
    Launches the Chrome browser, opens the OrangeHRM login page,
    maximizes the window, and closes the browser after the test.
    """
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    maximize_browser_window(driver)

    request.cls.driver = driver
    yield
    driver.quit()


def maximize_browser_window(driver):
    """
    Maximizes the browser window.
    """
    driver.maximize_window()
