import pytest
from ResetPasswordPage import ResetPasswordPage
from LoginPage import LoginPage
from logger_config import get_logger

logger = get_logger()


@pytest.mark.usefixtures("setup")
class TestLogin:
    driver = None
    reset_page: ResetPasswordPage
    login_page: LoginPage

    def test_reset_password(self):
        logger.info("Test started: Valid Login")
        self.reset_page = ResetPasswordPage(self.driver)

        assert self.reset_page.click_forget_password_button(), "Failed to click forget button"
        logger.info(f"Successfully clicked forget button")

        assert self.reset_page.enter_username("Admin"), "Failed to enter username"
        logger.info(f"Successfully entered username")

        assert self.reset_page.click_reset_password_button(), "Failed to click reset button"
        logger.info(f"Successfully clicked reset button")
