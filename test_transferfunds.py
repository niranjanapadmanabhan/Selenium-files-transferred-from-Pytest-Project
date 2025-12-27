import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def test_transfer():
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
    driver.find_element(By.XPATH,"//span[@id='transfer_funds_link']").click()
    time.sleep(2)
    ddm1=driver.find_element(By.NAME,"fromAccountId")
    first_ddm=Select(ddm1)
    first_ddm.select_by_index(1)
    time.sleep(2)
    ddm2 = driver.find_element(By.NAME,"toAccountId")
    second_ddm=Select(ddm2)
    second_ddm.select_by_index(2)
    time.sleep(2)
    driver.find_element(By.NAME,"amount").send_keys(100)
    driver.find_element(By.ID,"btn_submit").click()
    time.sleep(2)
    driver.find_element(By.ID, "btn_submit").click()
    time.sleep(2)
    alert=driver.find_element(By.XPATH,"//div[contains(text(),'You successfully submitted your transaction.')]").text
    if(alert=='You successfully submitted your transaction.'):
        print("Transaction completed successfully")
    else:
        print("Transaction failed, please retry after sometime.")