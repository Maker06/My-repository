from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser.get('https://play2048.co/')

htmlElem = browser.find_element_by_tag_name('html')
time.sleep(5)
i=0
for i in range(1,1000):
    htmlElem.send_keys(Keys.UP)
    time.sleep(1)
    htmlElem.send_keys(Keys.RIGHT)
    time.sleep(1)
    htmlElem.send_keys(Keys.DOWN)
    time.sleep(1)
    htmlElem.send_keys(Keys.LEFT)
    time.sleep(1)
    i = i + 1


