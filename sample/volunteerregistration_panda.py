import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains


capabilities = DesiredCapabilities.CHROME.copy()
capabilities['acceptInsecureCerts'] = True

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install(), desired_capabilities=capabilities))
driver.maximize_window()
driver.get("https://grameenavikassangham.org/RO-Water-Plant")
driver.find_element(By.XPATH,"//a[contains(text(),'Volunteer')]").click()
driver.get("https://grameenavikassangham.org/event-4108589/Registration")

email = (By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_email']")
next_button_email = (By.XPATH,"//input[@value='Next']")
wait_until_registration_form = (By.XPATH,"//h3[normalize-space()='Enter registration information']")
fullname = (By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl00_TextBox12578091']")
phone = (By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl02_TextBox12578096']")
chebox_health = (By.XPATH,"//span[@class='textLine'][normalize-space()='Health']")
programs_dropdown = (By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl04_DropDownList13023604']")
male_radio = (By.XPATH,"//span[contains(text(),'Male')]")
female_radio = (By.XPATH,"//span[contains(text(),'Female')]")
next_buton_form = (By.XPATH,"//input[@value='Next']")
confirm_button = (By.XPATH,"//input[@value='Confirm']")
registration_confirmation = (By.XPATH,"//h2[normalize-space()='Event registration: Confirmation (Receipt)']")

driver.find_element(*email).send_keys('raja@gmail.com')
driver.find_element(*next_button_email).click()
WebDriverWait(driver, 10).until(EC.presence_of_element_located(wait_until_registration_form))
driver.find_element(*fullname).send_keys('raja')
focus_areas = ['Health','Education','Agriculture','Environment','Spirituality','Skill Development']
for area in focus_areas:
    xpath = f"//span[@class='textLine'][normalize-space()='{area}']"
    print(xpath)
    checkbox = WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,xpath)))
    if not checkbox.is_selected():
        checkbox.click()
program_name = 'Free Computer Training Center'
dropdown = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl04_DropDownList13023604']")))
select = Select(dropdown)
select.select_by_visible_text(program_name)

gender = 'Female'
gender_radio = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,f"//span[contains(text(),'{gender}')]")))
gender_radio.click()

# calendar_icon = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl06_DateTextBox16390431_PU_TG']")))
calendar_textbox = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl06_DateTextBox16390431']")))
input_date = '24 Aug 2030'
calendar_textbox.send_keys(input_date)

driver.find_element(*next_buton_form).click()
time.sleep(3)





