from selenium import webdriver
import time
from selenium import *
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="D:\driver\chromedriver.exe")
driver.get("https://tarkov-market.com/ru/")
elem = driver.find_element_by_tag_name("input")
elem.send_keys("сигареты")
time.sleep(5)
elem1 = driver.find_elements_by_class_name("card")
# elem2 = elem1.find_element_by_class_name("cell alt")
for i in elem1:
    print(i.find_element_by_class_name("alt.big").text)

