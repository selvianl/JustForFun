from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
import time 


driver = webdriver.Firefox()
driver.get("https://www.amazon.com/")

#sing in butonuna tiklar
elem = driver.find_element_by_id('nav-link-accountList').click()


#mail adresini yazar
username = driver.find_element_by_id("ap_email")

username.send_keys("pierogist@yandex.com")
time.sleep(3)


#continue`ye tiklar
elem = driver.find_element_by_id("continue").click()


#sifreyi yazar
password = driver.find_element_by_id("ap_password")

password.send_keys("Ilikepierogi")
time.sleep(3)

#sign in e tiklar
elem = driver.find_element_by_id("signInSubmit").click()


# search`e samsung yazar
elem = driver.find_element_by_id("twotabsearchtextbox")

elem.send_keys("samsung")

# samsung kelimesini arar
elem = driver.find_element_by_class_name("nav-input").click()
time.sleep(3)

#samsung sayfasinda olduguna dair geri bildirim verir. Terminalde herhangi bir exception olmamasi dogru calistigini gosterir.
assert "samsung" in driver.title
time.sleep(3)
       

# 2.sayfaya tiklar
time.sleep(3)
elem = driver.find_element_by_class_name("pagnLink").click()


time.sleep(3)
page = driver.find_elements_by_xpath('.//span[@class = "pagnCur"]')[0].text

#2. sayfasinda olduguna dair geri bildirim verir. Terminalde herhangi bir exception olmamasi dogru calistigini gosterir.
assert page == '2'

# 3. urune tiklar
i = 0
for i in range (10):
	if i == 2:
		time.sleep(5)
		elemName = driver.find_elements_by_tag_name("h2")[i].text # Ileride geri bildirim almak icin secilen urunun adini tutar.
		elem = driver.find_elements_by_xpath("//img[contains(@src, 'images' )]/parent::a")[i].click()
		break
	else :
		i +=1
		continue

# add to list`e tiklar		
elem  = driver.find_element_by_id("add-to-wishlist-button-submit").click()
time.sleep(3)

# sag ok tusunu kullanarak wish list`i secer
checkboxes = driver.find_element_by_id("WLNEW_list_type_SL")
time.sleep(3)
checkboxes.send_keys(Keys.ARROW_RIGHT)

# submit`e tiklar
select = driver.find_elements_by_xpath('//input[@type="submit"]')
target = len(select)-1
select[target].click()

# Favorilere eklenen urun ile secilen urunun ayni oldugunu kontrol eder. Terminalde herhangi bir exception olmamasi dogru calistigini gosterir.
time.sleep(4)
elemWish = driver.find_elements_by_id("wl-huc-title-holder")[0].text
assert elemName == elemWish 
a = driver.find_element_by_link_text("View List").click()

time.sleep(4)
a = driver.find_element_by_link_text("Delete item").click()

#sayfayi yeniler ve urunun artik favorilerde olmadigini kontrol eder.  Terminalde herhangi bir exception olmamasi dogru calistigini gosterir.
driver.refresh()
time.sleep(3)
assert elemName not in driver.page_source





		
