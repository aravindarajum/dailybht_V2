import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# driver = webdriver.Chrome()
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # For Chrome version 109 and above
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

dataframe = pd.read_excel("C://Users//Lenovo//PycharmProjects//DailySolutionBHT_V2//sample//testdata.xlsx")


# Function to send email
def send_email(failed_cases):
    sender_email = "ajaypandy73@gmail.com"
    receiver_email = "aravind.raja@sociallygood.com"
    password = "tzsm adyi ggza yzwo"

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Failed Test Cases Report"

    body = "The following websites failed to load:\n\n" + "\n".join(failed_cases)
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# List to store failed cases
failed_cases = []

# Iterate through the rows in the DataFrame
for index, row in dataframe.iterrows():
    driver.get(row['url'])
    actual_title = driver.title
    expected_title = row['title']

    if actual_title == expected_title:
        dataframe.at[index, 'status'] = 'Pass'
    else:
        dataframe.at[index, 'status'] = 'Fail'
        failed_cases.append(row['url'])

# Save the updated DataFrame back to the Excel file
dataframe.to_excel("C://Users//Lenovo//PycharmProjects//DailySolutionBHT_V2//sample//testdata.xlsx", index=False)

# Send email if there are any failed cases
if failed_cases:
    send_email(failed_cases)

# Close the browser
driver.quit()
