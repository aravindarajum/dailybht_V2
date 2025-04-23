from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# Set up Edge options
edge_options = Options()
edge_options.add_argument("--headless")  # Enable headless mode

# Set up Firefox driver
service = EdgeService(EdgeChromiumDriverManager().install())
driver = webdriver.Edge(service=service, options=edge_options)

# Navigate to a webpage and print the title
driver.get("http://google.com")
print(driver.title)

# Quit the driver
driver.quit()
