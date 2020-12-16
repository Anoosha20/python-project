from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.countdown.co.nz/")
driver.maximize_window()
driver.implicitly_wait(6)
driver.find_element_by_xpath("//a[contains(@class,'navicon-shop')]").click()
childWindow = driver.window_handles[1]
driver.switch_to.window(childWindow)
dropdown = Select(driver.find_element_by_id("SearchType"))
dropdown.select_by_visible_text("Grocery")
action = ActionChains(driver)
driver.find_element_by_id("search").send_keys("fruit kiwi")



