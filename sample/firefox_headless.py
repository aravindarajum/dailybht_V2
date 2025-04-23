from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

# Set up Firefox options
firefox_options = Options()
firefox_options.add_argument("--headless")  # Enable headless mode

# Set up Firefox driver
service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=firefox_options)

# Navigate to a webpage and print the title
driver.get("http://google.com")
print(driver.title)

# Quit the driver
driver.quit()
