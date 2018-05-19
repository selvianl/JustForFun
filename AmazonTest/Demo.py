from WishList import *
import time

class Demo(unittest.TestCase):

    def setUp(self):
        self.driver = mypkg.CreateWebdriver()

    def test_Demo(self):
        time.sleep(3)
        self.driver.refresh()


if __name__ == "__main__":
    unittest.main()