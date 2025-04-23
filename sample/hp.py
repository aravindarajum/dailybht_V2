import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import DesiredCapabilities

capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

logo = (By.XPATH,"//p[@align='right']//font//img")
menu = (By.XPATH,"//*[@id='id_aPbl4fU']")
aboutus_label = (By.XPATH,"//p[text()='About GVS']")
footer_logo = (By.XPATH,"//div[@id='id_wxjYSbx']//img")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(), desired_capabilities=capabilities))
driver.maximize_window()
driver.get("https://grameenavikassangham.org/")
isLogoPresent = driver.find_element(*logo).is_displayed()
if isLogoPresent:
    print("Logo is found on Header section on Homepage")
else:
    print("Logo is NOT found on Header section on Homepage")

isMenuPresent = driver.find_element(*menu).is_displayed()
if isMenuPresent:
    print("Menu is found on Header section on Homepage")
else:
    print("Menu is NOT found on Header section on Homepage")

isAboutusLabelPresent = driver.find_element(*aboutus_label).is_displayed()
if isAboutusLabelPresent:
    print("About Us label is found on Header section on Homepage")
else:
    print("About Us label is NOT found on Header section on Homepage")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

isFooterLogoPresent = driver.find_element(*footer_logo).is_displayed()
if isFooterLogoPresent:
    print("Logo in footer is found on Footer section on Homepage")
else:
    print("Logo in footer is NOT found on Footer section on Homepage")

time.sleep(3)

