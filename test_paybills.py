from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time

def test_paybills():
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
    ddm=driver.find_element(By.NAME,"payee")
    first_ddm=Select(ddm)
    first_ddm.select_by_index(1)
    ddm1 = driver.find_element(By.NAME, "account")
    second_ddm = Select(ddm1)
    second_ddm.select_by_index(0)
    driver.find_element(By.NAME, "amount").send_keys(100)
    driver.find_element(By.NAME,"date").click()
    time.sleep(2)
    driver.find_element(By.XPATH,"//a[contains(text(),'27')]").click()
    time.sleep(2)
    driver.find_element(By.NAME,"description").send_keys("Test payment")
    driver.find_element(By.ID,"pay_saved_payees").click()
    time.sleep(2)
    alert=driver.find_element(By.XPATH,"//span[contains(text(),'The payment was successfully submitted.')]").text
    if(alert=='The payment was successfully submitted.'):
         print("Transaction completed successfully")
    else:
         print("Transaction failed, please retry after sometime.")