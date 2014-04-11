from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://orteil.dashnet.org/cookieclicker/")

while True:
    driver.find_element_by_id("bigCookie").click()

driver.close()
