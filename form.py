from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import select
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("the https://www.lambdatest.com/selenium-playground")

submit_btn = driver.find_element(By.LINK_TEXT,"Input form submit").click()
submit_btn.click()

name_field = driver.find_element(By.ID,"name")
 assert validation_msg == "please fill out this field ","validation message did not match"
 print(" Validation message verified ")

 driver.find_element(By.NAME,"name").send_keys("John Doe")
 driver.find_element(By.NAME,"email").send_keys("johndoe@example.com")
 driver.find_element(By.NAME,"password").send_keys("Test@123")
 driver.find_element(By.NAME,"company").send_keys("Test Company")
 driver.find_element(By.NAME,"website").send_keys("https://example.com")

 country_dropdown = select(driver.find_element(By.Name,"country")
 country_dropdown.select_by_visible_text("United States")

 driver.find_element(By.NAME,"country").send_keys("New York")
 driver.find_element(By.NAME,"address1").send_keys("123 test street")
 driver.find_element(By.NAME,"address2").send_keys("suit 45")
 driver.find_element(By.NAME,"state").send_keys("NY")
 driver.find_element(By.NAME,"zip").send_keys("10001")

submit_btn.click()
time.sleep(2)

success_msg = driver.find_element(By.CSS_SELECTOR,"p.success-msg").text
assert success_msg == "thanks for contacting us ,we will get back to you shortly.","Success message did not match"
print("Success message verified ")

driver.quit()
