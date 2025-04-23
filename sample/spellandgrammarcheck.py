from selenium import webdriver
import requests
from selenium.webdriver.common.by import By

# Start Selenium WebDriver
driver = webdriver.Chrome()
driver.get("https://sac.sewausa.org/?theme=3139")

# Extract visible text
text = driver.find_element(By.TAG_NAME, "body").text

# Use LanguageTool API for checking
response = requests.post(
    'https://api.languagetoolplus.com/v2/check',
    data={'text': text, 'language': 'en'}
)
print(response.json())

driver.quit()
