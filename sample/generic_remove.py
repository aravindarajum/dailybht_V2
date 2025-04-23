from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://sakshamseva.wildapricot.org/")
driver.find_element(By.XPATH,"//p[contains(text(),'SAKSHAM')]")