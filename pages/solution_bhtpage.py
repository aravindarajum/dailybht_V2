from pages.basedriver import BaseDriver
from utils.utilities import Utilities
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

testdata_file = "testdata/ngos.xlsx"


class solutions_bht(BaseDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        custom_logger = Utilities(self.driver)
        self.log = custom_logger.get_logger()

    def solBHT(self):
        custom_logger = Utilities(self.driver)
        self.log = custom_logger.get_logger()
        basedriver = BaseDriver(self.driver)

        dataframe = pd.read_excel(testdata_file)
        # Ensure the 'status' column can accommodate string values
        dataframe['status'] = dataframe['status'].astype('object')
        # List to store failed cases
        failed_cases = []
        # Iterate through the rows in the DataFrame
        try:
            for index, row in dataframe.iterrows():
                self.driver.get(row['url'])
                actual_title = self.driver.title
                expected_title = row['title']

                if actual_title == expected_title:
                    dataframe.at[index, 'status'] = 'Pass'
                    self.log.info(f"{row['url']} loaded successfully.")
                    basedriver.capture_screenshot(row['ngoname'])
                    dataframe.to_excel(testdata_file, index=False)
                else:
                    dataframe.at[index, 'status'] = 'Fail'
                    failed_cases.append(row['url'])
                    self.log.error(f"{row['url']} NOT loaded.")
                    basedriver.capture_screenshot(row['ngoname'])
                    dataframe.to_excel(testdata_file, index=False)

        # Save the updated DataFrame back to the Excel file
        # dataframe.to_excel(testdata_file, index=False)
        except Exception:
            self.log.error(f"Looks like, a URL not loading {self.driver.get(row['url'])}")

        # Send email if there are any failed cases
        if failed_cases:
            custom_logger.send_email(failed_cases)

    # def send_email(self, failed_cases):
    #     sender_email = "helpdesk@sociallygood.com"
    #     receiver_email = ["aravind.raja@sociallygood.com", "aravinda.ec@gmail.com"]
    #     password = "oqlf mhpc czwe ionb"
    #
    #     message = MIMEMultipart()
    #     message["From"] = sender_email
    #     message["To"] = ", ".join(receiver_email)
    #     message["Subject"] = "Failed Test Cases Report"
    #
    #     body = "The following websites failed to load:\n\n" + "\n".join(failed_cases)
    #     message.attach(MIMEText(body, "plain"))
    #
    #     with smtplib.SMTP("smtp.gmail.com", 587) as server:
    #         server.starttls()
    #         server.login(sender_email, password)
    #         server.sendmail(sender_email, receiver_email, message.as_string())
