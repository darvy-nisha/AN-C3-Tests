import pytest
from LoginPage import Login



@pytest.mark.usefixtures("setup")
class TestLogin:
    driver = None

    def test_001_valid_login(self):
        lg = Login(self.driver)
        lg.input_username("Admin")
        lg.input_password("Admin123")
        lg.click_login()
        # (assert dashboard later)

    def test_002_invalid_username(self):
        lg = Login(self.driver)
        lg.input_username("Amin")
        lg.input_password("Admin123")
        lg.click_login()

        assert "Invalid credentials" in lg.invalid_mssg()

    def test_003_invalid_password(self):
        lg = Login(self.driver)
        lg.input_username("Admin")
        lg.input_password("Admin12")
        lg.click_login()
        assert 'Invalid credentials' in lg.invalid_mssg(), "Failed to login"
