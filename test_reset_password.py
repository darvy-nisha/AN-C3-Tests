import pytest
from ResetPasswordPage import ResetPasswordPage
from logger_config import get_logger

logger = get_logger()


@pytest.mark.usefixtures("setup")
class TestLogin:
    """
    Test cases related to login and reset password functionality.
    """

    driver = None
    reset_page: ResetPasswordPage

    def test_reset_password(self):
        logger.info("Test started: Reset Password flow")

        self.reset_page = ResetPasswordPage(self.driver)

        assert self.reset_page.click_forget_password_button(), "Failed to click the 'Forgot Password' button"
        logger.info("Successfully clicked the 'Forgot Password' button")

        assert self.reset_page.enter_username("Admin"), "Failed to enter the username"
        logger.info("Successfully entered the username")

        assert self.reset_page.click_reset_password_button(), "Failed to click the reset password button"
        logger.info("Successfully clicked the reset password button")
