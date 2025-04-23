from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from webdriver_manager.microsoft import EdgeChromiumDriverManager


# firefox_options = Options()
# firefox_options.add_argument("--headless")
# service = FirefoxService(GeckoDriverManager().install())
# driver = webdriver.Firefox(service=service, options=firefox_options)


# ------------------ Chrome Browser Headless Script -----------------------------------------
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
# ------------------ Chrome Browser Headless Script -----------------------------------------

# ------------------ Firefox Browser Headless Script -----------------------------------------
# firefox_options = Options()
# firefox_options.add_argument("--headless")
# driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
# ------------------ Firefox Browser Headless Script -----------------------------------------


# ------------------ Edge Browser Headless Script -----------------------------------------
# edge_options = Options()
# edge_options.add_argument("--headless")
# driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()), options=edge_options)
# ------------------ Edge Browser Headless Script -----------------------------------------


# -------------------------------Full script ---------------------------------------
# capabilities_chrome = DesiredCapabilities.CHROME.copy()
# capabilities_firefox = DesiredCapabilities.FIREFOX.copy()
# capabilities_edge = DesiredCapabilities.EDGE.copy()
#
#
# capabilities_chrome['acceptInsecureCerts'] = True
# capabilities_firefox['acceptInsecureCerts'] = True
# capabilities_edge['acceptInsecureCerts'] = True

browser = input('type browser name : ')

if browser == "chrome":
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # For Chrome version 109 and above
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options)
elif browser == "firefox":
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Enable headless mode
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=firefox_options)
elif browser == "edge":
    edge_options = Options()
    edge_options.add_argument("--headless")  # Enable headless mode
    service = EdgeService(EdgeChromiumDriverManager().install())
    driver = webdriver.Edge(service=service, options=edge_options)

# -------------------------------Full script ---------------------------------------


driver.maximize_window()
driver.get("https://google.com/")
print(driver.title)
driver.quit()
