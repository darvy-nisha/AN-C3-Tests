import pytest
from LoginPage import LoginPage
from logger_config import get_logger

logger = get_logger()

@pytest.mark.usefixtures("setup")
class TestLogin:
    driver = None

    def test_001_valid_login(self):
        logger.info("Test started: Valid Login")

        lg = LoginPage(self.driver)

        assert lg.input_username(username="Admin"), "Failed to input username"
        logger.info("Username entered successfully")

        assert lg.input_password(password="Admin123"), "Failed to input password"
        logger.info("Password entered successfully")

        assert lg.click_login(), "Failed to click login"
        logger.info("Login successful")

    def test_002_invalid_username(self):
        logger.info("Test started: Invalid Username")

        lg = Login(self.driver)

        assert lg.input_username("Amin"), "Failed to input invalid username"
        logger.info("Invalid username entered")

        assert lg.input_password("Admin123"), "Failed to input password"
        logger.info("Password entered successfully")

        assert lg.click_login(), "Failed to click login"
        logger.info("Login button clicked")


        assert "Invalid credentials" in lg.invalid_mssg(), "Failed to input invalid username"
        logger.info("Invalid username entered")



