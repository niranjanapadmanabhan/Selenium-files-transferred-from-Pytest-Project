from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Global variable because everytime we initialize chrome, the winow will close and open and login script on't be executed in createcourse function.
driver = webdriver.Chrome()
driver.maximize_window()
#driver.implicitly_wait(10)
def test_login():
    driver.get("http://www.ezhrs.com/ezCourses/admin/admin.asp?action=admin")
    driver.find_element(By.NAME, "uname").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("pass")
    driver.find_element(By.NAME, "SUBMIT").click()

def test_createcourse():
    driver.find_element(By.LINK_TEXT, "Schedule Courses").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Create New Course").click()

    #time.sleep(5)
    ddm1 = Select(driver.find_element(By.NAME, "Cat"))

    ddm1.select_by_index(2)

    driver.find_element(By.NAME, "Title").send_keys("excel211")

    ddm2 = Select(driver.find_element(By.NAME, "course_Level"))
    ddm2.select_by_index(1)
    driver.find_element(By.NAME, "Description").send_keys("i love qa ")
    description = driver.find_element(By.NAME, "Description").get_attribute("value")

    print(description)
    # Finding the element Certificate
    cert = driver.find_element(By.XPATH, value="//input[@name='Cert']")
    cert.click()
    time.sleep(5)
# Finding element for Create Course button
    create = driver.find_element(By.NAME, value="Submit")
    create.click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "excel211").click()
    time.sleep(5)

    description2= driver.find_element(By.NAME, "Description").get_attribute("value")

    if (description2 == description):
        print("test case passed")
    else:
        print("test case failed")