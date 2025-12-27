from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time

@pytest.mark.parametrize("invalid_date",[(""),
                                         ("12-13-2024"),
                                         ("2025-02-29")])
def test_paybills(invalid_date):
    driver=webdriver.Chrome()
    driver.get("http://zero.webappsecurity.com/index.html")
    driver.maximize_window()
    driver.find_element(By.ID,"signin_button").click()
    driver.find_element(By.NAME,"user_login").send_keys("username")
    driver.find_element(By.NAME, "user_password").send_keys("password")
    driver.find_element(By.NAME,"user_remember_me").click()
    driver.find_element(By.NAME, "submit").click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.find_element(By.ID,"online-banking").click()
    time.sleep(2)
    driver.find_element(By.ID,"pay_bills_link").click()
    time.sleep(2)
    driver.find_element(By.NAME,"date").send_keys(invalid_date)
    time.sleep(2)
    value=driver.find_element(By.NAME,"date").get_attribute("value")
    time.sleep(2)
    print("Date in invalid format is:",value)
    time.sleep(2)
