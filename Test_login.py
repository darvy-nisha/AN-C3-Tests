import pytest
from PageObjects.LoginPage import Login
import time



@pytest.mark.usefixtures("setup")
class Testlogin:



    def test_001(self):
        lg=Login(self.driver)
        lg.input_username("Admin")
        lg.input_password("Admin123")
        lg.click_login()
        time.sleep(10)



    def test_002(self):
        lg = Login(self.driver)
        lg.input_username("Amin")
        lg.input_password("Admin123")
        lg.click_login()

        time.sleep(10)
        if 'Invalid credentials' in lg.invalid_mssg():
            assert True
        else:
            assert False


    def test_003(self):
        lg = Login(self.driver)
        lg.input_username("Admin")
        lg.input_password("Admin12")
        lg.click_login()
        time.sleep(10)
        if 'Invalid credentials' in lg.invalid_mssg():
            assert True
        else:
            assert False
