import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(), desired_capabilities=capabilities))
driver.maximize_window()
driver.get("https://grameenavikassangham.org/")

focusareas_menu = (By.XPATH,"//li[@class='dir']//span[contains(text(),'Focus Areas')]")
focusarea_label = (By.XPATH,"//p[text()='Focus Areas']")
health_label = (By.XPATH,"//a[text()='Health']")
education_section = (By.XPATH,"//*[@id='id_J5wUjhg']/table/tbody/tr")
education_label = (By.XPATH,"//a[text()='Education']")
health_section = (By.XPATH,"//*[@id='id_pR9brsG']/table/tbody/tr")
viewprograms_button = (By.XPATH,"//a[@href='/Health'][normalize-space()='View Programs']")



driver.find_element(*focusareas_menu).click()
isfocusareaa_label_present = driver.find_element(*focusarea_label)
print("clicked on Focus Area menu")
if isfocusareaa_label_present:
    print("focusarea_label found")
else:
    print("focusarea_label NOT found")

ishealth_label_present = driver.find_element(*health_label)
if ishealth_label_present:
    print("health_label found")
else:
    print("health_label NOT found")

actions = ActionChains(driver)
education_sect = WebDriverWait(driver, 10).until(EC.presence_of_element_located(education_section))
actions.move_to_element(education_sect).perform()
print("Scrolled to education section")

iseducation_label_present = driver.find_element(*education_label)
if iseducation_label_present:
    print("education_label found")
else:
    print("education_label NOT found")

health_sect = WebDriverWait(driver, 10).until(EC.presence_of_element_located(health_section))
actions.move_to_element(health_sect).perform()
print("Scrolled to health_section")

driver.find_element(*viewprograms_button).click()
print("viewprograms_button clicked")






