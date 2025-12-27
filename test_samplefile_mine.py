from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest


driver = webdriver.Chrome()
driver.get("http://ezhrs.com/project1/ezcourses/admin/admin.asp?action=admin")
driver.maximize_window()
time.sleep(2)


def test_studentlist():

    # login
    uname = driver.find_element(By.NAME, value="uname")
    # Typing username
    uname.send_keys("admin")
    # Finding element for password
    paswd = driver.find_element(By.NAME, value="password")
    # Typing password
    paswd.send_keys("pass")
    # Finding element for Login button
    login = driver.find_element(By.NAME, value="SUBMIT")
    # To click the button login
    login.click()
    time.sleep(3)
    # click students hyperlink
    driver.find_element(By.LINK_TEXT, "Students").click()
    time.sleep(5)
    # click students list hyperlink
    driver.find_element(By.LINK_TEXT, "Student List").click()
    time.sleep(3)
    displayed = driver.find_element(By.XPATH,"//a[contains(text(),'P Niranj')]").text
    print("Displayed student names are:",displayed)

