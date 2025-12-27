import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_login():
    driver=webdriver.Chrome()
    driver.get("http://zero.webappsecurity.com/index.html")
    driver.maximize_window()
    driver.find_element(By.ID,"signin_button").click()
    driver.find_element(By.NAME,"user_login").send_keys("username")
    uname=driver.find_element(By.NAME,"user_login").get_attribute("value")
    print("Username entered is:",uname)
    driver.find_element(By.NAME, "user_password").send_keys("password")
    driver.find_element(By.NAME,"user_remember_me").click()
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    displayed_name=driver.find_element(By.XPATH,"//body/div[1]/div[1]/div[1]/div[1]/div[1]/ul[1]/li[3]/a[1]").text
    print("the displayed name is:",displayed_name)
    if (uname==displayed_name):
        print("Test case passed")
    else:
        print("Test case failed")

