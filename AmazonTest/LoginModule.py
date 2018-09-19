import unittest
import mypkg


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = mypkg.CreateWebdriver()
        self.driver.get("http://www.amazon.com")

    def test_login(self):
        driver = self.driver
        elem = driver.find_element_by_id('nav-link-accountList').click()
        username = driver.find_element_by_id("ap_email")

        username.send_keys("mail_here")
        elem = driver.find_element_by_id("continue").click()

        password = driver.find_element_by_id("ap_password")
        password.send_keys("password_here")

        elem = driver.find_element_by_id("signInSubmit").click()


if __name__ == "__main__":
    unittest.main()
