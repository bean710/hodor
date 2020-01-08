from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Firefox()

browser.get("http://158.69.76.135/level1.php")

for i in range (4096 // 8):
	textbox = browser.find_element_by_name("id")
	submit = browser.find_element_by_name("holdthedoor")
	textbox.send_keys("1052")
	submit.click()

browser.close()
