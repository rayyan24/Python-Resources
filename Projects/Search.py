from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
#set chromodriver.exe path
search=input("Enter Search Keyword: ")
driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
# driver = webdriver.Edge()
driver.maximize_window()
# driver.implicitly_wait(0.5)
#launch URL
driver.get("https://www.google.com/")
#identify search box
m = driver.find_element_by_name("q")
#enter search text
m.send_keys(search)
time.sleep(0.2)
#perform Google search with Keys.ENTER
m.send_keys(Keys.ENTER)
