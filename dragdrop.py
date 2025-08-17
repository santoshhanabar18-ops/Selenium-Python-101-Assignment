from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
 driver= webdriver.Chrome()
 driver.maximize_window()
 driver.get("https://www.lambdatest.com/selenium-playground")
 driver.find_element(By.LINK_TEXT,"Drag and Drop Sliders").click()
 slider = driver.find_element(By.ID,"rangeSuccess")
 actions = ActionChains(driver)
 while range_value.text !="95":
     actions.drag_and_drop_by(slider,5,0).perform()
     time.sleep(0.1)
 assert range_value.text == "95", f"test failed! current value: {range_value.text}"
 print("test passed")
 driver.quit()
