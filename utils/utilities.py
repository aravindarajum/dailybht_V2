import inspect
import pandas as pd

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
# import openpyxl
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Utilities:
    def __init__(self, driver):
        self.driver = driver

    def get_logger(self, logLevel=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logLevel)
        file_handler = logging.FileHandler('logs/test_log.log')
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger

    def send_email(self, failed_cases):
        sender_email = "helpdesk@sociallygood.com"
        receiver_email = ["aravind.raja@sociallygood.com", "aravinda.ec@gmail.com"]
        password = "oqlf mhpc czwe ionb"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = ", ".join(receiver_email)
        message["Subject"] = "Failed Test Cases Report"

        body = "The following websites failed to load:\n\n" + "\n".join(failed_cases)
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

    # def read_data_from_excel(self, workbook_name):
    #     dataframe = pd.read_excel(workbook_name)
    #     data = []
    #     for row in dataframe.index:
    #         entry = dataframe.iloc[row]
    #         data.append(entry)
    #     return data

    # def custom_wait_for_element(self, locator, timeout=10):
    #     return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))


