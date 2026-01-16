import pytest
from LoginPage import LoginPage
from logger_config import get_logger

logger = get_logger()

@pytest.mark.usefixtures("setup")
class TestLogin:
    driver = None

    def test_001_valid_login(self):
        logger.info("Test started: Valid Login")

        login_page = LoginPage(self.driver)

        assert login_page.input_username(username="Admin"), "Failed to input username"
        logger.info("Username entered successfully")

        assert login_page.input_password(password="Admin123"), "Failed to input password"
        logger.info("Password entered successfully")

        assert login_page.click_login(), "Failed to click login"
        logger.info("Login successful")

    def test_002_invalid_username(self):
        logger.info("Test started: Invalid Username")

        login_page = LoginPage(self.driver)

        assert login_page.input_username("Amin"), "Failed to input invalid username"
        logger.info("Invalid username entered")

        assert login_page.input_password("Admin123"), "Failed to input password"
        logger.info("Password entered successfully")

        assert login_page.click_login(), "Failed to click login"
        logger.info("Login button clicked")


        assert "Invalid credentials" in login_page.invalid_mssg(), "Failed to input invalid username"
        logger.info("Invalid username entered")



