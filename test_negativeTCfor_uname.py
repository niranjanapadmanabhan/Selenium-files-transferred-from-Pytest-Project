import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


@pytest.mark.parametrize("uname,pwd",[("","password"),
                                        ("AQWERTYUI","password"),
                                        ("!@#$%^&*","password")])

def test_negative(uname,pwd):
    driver = webdriver.Chrome()
    driver.get("http://zero.webappsecurity.com/index.html")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID, "signin_button").click()
    # driver.find_element(By.NAME, "user_login").clear()
    driver.find_element(By.NAME, "user_login").send_keys(uname)
    time.sleep(2)
    driver.find_element(By.NAME, "user_password").send_keys(pwd)
    time.sleep(2)
    driver.find_element(By.NAME, "user_remember_me").click()
    driver.find_element(By.NAME, "submit").click()
    error_msg=driver.find_element(By.XPATH,"//div[contains(text(),'Login and/or password are wrong.')]").text
    time.sleep(3)
    if(error_msg=='Login and/or password are wrong.'):
        print("Login failed")
    else:
        print("Login successful")
    time.sleep(2)



