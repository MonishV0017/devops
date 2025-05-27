from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_driver_path= 'D:\chromedriver-win64\chromedriver.exe'  # Update this path to your chromedriver location
service = Service(executable_path=chrome_driver_path)
driver= webdriver.Chrome(service=service)
driver.get('https://www.google.com') 
assert "Gogle" in driver.title
time.sleep(5) # Replace with your target URL
driver.quit()  # Close the browser after the task is done