from logging import error
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
chrome_options = Options()
chrome_options.add_argument("--start-maximized")
#chrome_options.add_argument("--headless")

PATH = "/home/ubuntu/Desktop/chromedriver"
driver = webdriver.Chrome(PATH, chrome_options=chrome_options)
driver.get("https://www.google.com/maps")
search = driver.find_element_by_id("searchboxinput")
search.send_keys('al reem island, A3 Tower')
search.send_keys(Keys.RETURN)
window_before = driver.window_handles[0]
time.sleep(5)

e = driver.find_element_by_xpath("/html/body/jsl/div[3]/div[9]/div[1]/div[3]/canvas")
w_val = e.get_attribute("width")
h_val = e.get_attribute("height")
action = webdriver.common.action_chains.ActionChains(driver)
w_error = 220
h_error = 18
action.move_to_element_with_offset(e, (int(w_val)/2) - w_error, (int(h_val)/2) - h_error)
action.context_click()
action.perform()

#Edit the offset error value according to the window size 