from selenium import webdriver


# Set up Chrome options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")  # For Chrome version 109 and above
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
# service = ChromeService(ChromeDriverManager().install())

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)
# driver = webdriver.Chrome(service=service,options=chrome_options)
# Open a webpage
driver.get("https://www.google.com")

# Perform actions on the webpage
print(driver.title)

# Close the browser
driver.quit()
