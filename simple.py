from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.lambdatest.com/selenium-playground")
driver.find_element(By.LINK_TEXT,"Simple form demo").click()
assert "Simple-form-demo" in driver.current_url, "Url validation failed"
message = "Welcome to Lambda Test"
input_box= driver.find_element(By.ID, "showInput").click()
displayed_messsage = driver.find_element(By.ID,"message").text
assert displayed_messsage == message,f"Expected {message}, but got {displayed_messsage}"
driver.quit()




