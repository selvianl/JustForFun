from LoginModule import *

class Search(unittest.TestCase):

    def setUp(self):
        self.driver = mypkg.CreateWebdriver()

    def test_search (self):

        elem = self.driver.find_element_by_id("twotabsearchtextbox")

        elem.send_keys("samsung")

        elem = self.driver.find_element_by_class_name("nav-input").click()

        assert "samsung" in self.driver.title

if __name__ == "__main__":
    unittest.main()

