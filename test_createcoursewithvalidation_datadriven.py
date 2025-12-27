from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import pytest


@pytest.mark.parametrize("category,title",[("1","computer911"),
                                           ("2","computer922"),
                                           ("3","computer933")])

def test_createcoursedd(category,title):
    driver = webdriver.Chrome()
    driver.get("http://ezhrs.com/project1/ezcourses/admin/admin.asp?action=admin")
    driver.find_element(By.NAME, "uname").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("pass")
    driver.find_element(By.NAME, "SUBMIT").click()
    driver.find_element(By.LINK_TEXT, "Schedule Courses").click()
    time.sleep(5)
    driver.find_element(By.LINK_TEXT, "Create New Course").click()

    time.sleep(5)
    ddm1 = Select(driver.find_element(By.NAME, "Cat"))

    ddm1.select_by_value(category)

    driver.find_element(By.NAME, "Title").send_keys(title)
    title1 = driver.find_element(By.NAME, "Title").get_attribute("value")
    print(title1)

    ddm2 = Select(driver.find_element(By.NAME, "course_Level"))
    ddm2.select_by_index(1)
    driver.find_element(By.NAME, "Description").send_keys("54321")

    driver.find_element(By.NAME, "Cert").click()

    driver.find_element(By.NAME, "Submit").click()

    course = driver.find_element(By.LINK_TEXT, title).text
    print(course)
    #
    # if (title1 == course):
    #     print("test case passed")
    # else:
    #     print("test case failed")

    driver.close()


