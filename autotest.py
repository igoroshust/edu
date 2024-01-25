# python3 -m pip install selenium

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from time import sleep

driver = webdriver.Chrome()
driver.get("https://google.com")
# driver.get("http://130.193.37.179/app/pets")
# (driver.find_elements(By.XPATH, "//*[@id=\"image\"]/img"))[0].click()
driver.find_element(By.XPATH, "//textarea[@title=\"Поиск\"]").send_keys('Skillfactory' + Keys.RETURN) # относится к google
sleep(2) # относится к google
driver.save_screenshot('sf.png') # относится к google
driver.quit()

sleep(3)
print(4)
print(5)
print(6)
a = [i**2 for i in range(10)]
print(a)


# //*[@id="APjFqb"]