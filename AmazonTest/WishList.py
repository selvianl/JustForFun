from SearchModule import *
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys


class WishList(unittest.TestCase):

    def setUp(self):
        self.driver = mypkg.CreateWebdriver()

    def test_WishList(self):
        elem = self.driver.find_element_by_class_name("pagnLink").click()
        #page = self.driver.find_elements_by_xpath('.//span[@class = "pagnCur"]')[0].text
        #assert page == '2'
        i = 0
        for i in range (10):
            if i == 2:
                time.sleep(3)
                #elemName = self.driver.find_elements_by_tag_name("h2")[i].text # Ileride geri bildirim almak icin secilen urunun adini tutar.
                elem = self.driver.find_elements_by_xpath("//img[contains(@src, 'images' )]/parent::a")[i].click()
                break
            else :
                i +=1
                continue

        elem = WebDriverWait(self.driver,4).until(EC.presence_of_element_located((By.ID , "add-to-wishlist-button-submit")))
        elem = self.driver.find_element_by_id("add-to-wishlist-button-submit")

        if "customer review" in self.driver.title:
                wishlist = WebDriverWait(self.driver,4).until(EC.presence_of_element_located((By.ID , "a-autoid-2-announce")))

                wishlist = self.driver.find_element_by_id("a-autoid-2-announces").click()
                print("1")

                whislist = WebDriverWait(self.driver,4).until(EC.presence_of_element_located((By.CLASS_NAME , "w-button-text")))

                wishlist = self.driver.find_element_by_class_name("w-button-text").click()
                print("2")
                deleting = WebDriverWait(self.driver,4).until(EC.presence_of_element_located((By.LINK_TEXT, 'Delete item')))

                deleting = self.driver.find_element_by_link_text("Delete item").click()
                print("3")


        try:
            checkboxes = WebDriverWait(self.driver,3).until(EC.presence_of_element_located((By.ID, "WLNEW_list_type_SL")))

            checkboxes= self.driver.find_element_by_id("WLNEW_list_type_SL")
            checkboxes.send_keys(Keys.ARROW_RIGHT)

            select = self.driver.find_elements_by_xpath('//input[@type="submit"]')
            target = len(select)-1
            select[target].click()

        except TimeoutException:
            print ("Loading took too much time!")




        try:
            a = WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.LINK_TEXT, 'View List')))
            print ("Page is ready!")
            a = self.driver.find_element_by_link_text("View List").click()

            deleting =  WebDriverWait(self.driver,5).until(EC.presence_of_element_located((By.LINK_TEXT, 'Delete item')))
            deleting = self.driver.find_element_by_link_text("Delete item").click()
        except TimeoutException:
            print ("Loading took too much time!")





if __name__ == "__main__":
    unittest.main()