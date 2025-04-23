import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# class readexcelusingpandas:
#     def read_data_from_excel(self,workbook_name):
#         dataframe = pd.read_excel(workbook_name)
#         data = []
#         for row in dataframe.index:
#             entry = dataframe.iloc[row]
#             data.append(entry)
#         return data
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://grameenavikassangham.org/event-4108589/Registration")
emailid = (By.XPATH, "//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_email']")
next_button_email = (By.XPATH, "//input[@value='Next']")
volunteer_fullname = (By.XPATH,
                           "//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl00_TextBox12578091']")
phone = (By.XPATH,
              "//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_registrationForm_eventRegistrationFormRepeater_ctl02_TextBox12578096']")
health_checkbox = (By.XPATH, "//span[@class='textLine'][normalize-space()='Health']")
education_checkbox = (By.XPATH, "//span[@class='textLine'][normalize-space()='Education']")
agriculture_checkbox = (By.XPATH, "//span[@class='textLine'][normalize-space()='Agriculture']")
environment_checkbox = (By.XPATH, "//span[@class='textLine'][normalize-space()='Environment']")
skill_development_checkbox = (By.XPATH, "//span[@class='textLine'][normalize-space()='Skill Development']")
spirituality_checkbox = (By.XPATH, "//span[@class='textLine'][normalize-space()='Spirituality']")

# pandaobject = readexcelusingpandas()
dataframe = pd.read_excel('C://Users//Lenovo//PycharmProjects//GrameenaVikasSangham_V3//testdata//registrants_data.xlsx')

for i in dataframe.index:
    entry = dataframe.iloc[i]
    driver.find_element(By.XPATH,"//*[@id='FunctionalBlock1_ctl00_eventPageViewBase_ctl00_ctl00_stepTemplate_email']").send_keys(entry['email'])
    driver.find_element(*next_button_email).click()
    # driver.find_element(*volunteer_fullname).send_keys(entry['fullname'])
    # print(entry['fullname'])
    # print(entry['email'])
    # print(entry['focusareas'])
    focus_list = list(entry['focusareas'].split(','))
    for each_checkbox in focus_list:
        print('each_checkbox:',each_checkbox)
        driver.find_element(By.XPATH,f"//span[@class='textLine'][normalize-space()='{each_checkbox}']").click()
    # print(f"data type of focus areas:{type(entry['focusareas'])} ")
    print('focus_list type',type(focus_list))
    print(focus_list)



# excel_data = pandaobject.read_data_from_excel("C://Users//Lenovo//PycharmProjects//GrameenaVikasSangham_V2//testdata//registrants_data.xlsx")
# print(excel_data)