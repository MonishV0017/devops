from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("http://www.yahoo.com")
assert 'Yahoo' in browser.title
elem = browser.find_element(By.NAME, 'p')
elem.send_keys('selenium' + Keys.RETURN)
time.sleep(5)
browser.close()
browser.quit()