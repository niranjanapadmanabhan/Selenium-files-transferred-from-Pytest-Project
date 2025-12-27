import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


def test_schedule_dd():


    # Global variable because everytime we initialize chrome, the winow will close and open and login script on't be executed in createcourse function.
    driver = webdriver.Chrome()
    driver.maximize_window()

    # driver.implicitly_wait(10)
    def test_login():
        driver.get("http://ezhrs.com/project1/ezcourses/admin/admin.asp?action=admin")
        driver.find_element(By.NAME, "uname").send_keys("admin")
        driver.find_element(By.NAME, "password").send_keys("pass")
        driver.find_element(By.NAME, "SUBMIT").click()

    # schedule course
    def test_schdedule():
        time.sleep(3)

        driver.maximize_window()
        driver.find_element(By.LINK_TEXT, "Schedule Courses").click()

        time.sleep(5)
        driver.find_element(By.XPATH, "//tbody/tr[19]/td[5]/div[1]/a[1]/img[1]").click()
        time.sleep(5)

        course = driver.find_element(By.XPATH,
                                     "//body[1]/table[2]/tbody[1]/tr[1]/td[1]/div[1]/form[1]/center[1]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/b[1]").text
        print(course)

        # course1 = course[23:]
        # print(course1)

        ddm_instructor = Select(driver.find_element(By.NAME, "instructor"))
        ddm_instructor.select_by_value("1")
        time.sleep(1)

        ddm_location = Select(driver.find_element(By.NAME, "ClassID"))
        ddm_location.select_by_value("1")
        time.sleep(1)

        ddm_office = Select(driver.find_element(By.NAME, "OfficeID"))
        ddm_office.select_by_value("2")
        time.sleep(1)

        date_input = driver.find_element(By.NAME, "firstinput").send_keys("2035/08/24")
        time.sleep(1)

        ddm_time = driver.find_element(By.XPATH, "//tbody/tr[1]/td[2]/div[1]/select[1]/option[4]").click()
        time.sleep(1)

        ddm_duration = Select(driver.find_element(By.NAME, "duration"))
        ddm_duration.select_by_value("4")
        time.sleep(1)

        ddm_limit = Select(driver.find_element(By.NAME, "Limit"))
        ddm_limit.select_by_value("15")
        time.sleep(1)

        driver.find_element(By.NAME, "btnCourse").click()

        driver.refresh()

        time.sleep(5)

        ## active course page

        displayed = driver.find_element(By.LINK_TEXT, "01111").text
        print(displayed)

        if (course1 == displayed):
            print("test case passed")
        else:
            print("test case failed")

    # logout
    def test_logout():
        driver.quit()





