import os
import time

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils.utilities import Utilities

custom_logger = Utilities(driver=webdriver)
log = custom_logger.get_logger()
@pytest.fixture(scope="class")
def setup(request):
    global driver

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")  # For Chrome version 109 and above
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Chrome(options=chrome_options)

    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()

def pytest_html_report_title(report):
    report.title = "Daily Solutions BHT"


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])
    if report.when == "call":
        xfail = hasattr(report, "wasxfail")
        if (report.skipped and xfail) or (report.failed and not xfail):
            # only add additional html on failure
            report_directory = os.path.dirname(item.config.option.htmlpath)
            file_name = str(int(round(time.time() * 1000))) + ".png"
            # file_name = report.nodeid.replace("::", "_") + ".png"
            destinationFile = os.path.join(report_directory, file_name)
            driver.save_screenshot(destinationFile)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:300px;height=200px" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
            extras.append(pytest_html.extras.html(html))
        report.extras = extras



