from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.countdown.co.nz/")
driver.maximize_window()
try:
    driver.find_element_by_xpath("//label[@class='doNotShowEasyEmailSignupDialog']//input").click()
    driver.find_element_by_xpath("//span[contains(text(),'×')]").click()
except Exception as e:
    print(e)
driver.implicitly_wait(6)
driver.find_element_by_xpath("//a[contains(@class,'navicon-shop')]").click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
driver.find_element_by_xpath("//ul[@class='toolbar-links-items nav']/li[2]/button").click()
driver.find_element_by_link_text("Fruit & Veg").click()






