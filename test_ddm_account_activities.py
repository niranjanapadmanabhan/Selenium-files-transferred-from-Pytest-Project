from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pytest
import time

def test_ddmaccount():
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
    driver.find_element(By.XPATH,"//span[@id='account_activity_link']").click()
    time.sleep(2)
    ddm=driver.find_element(By.NAME,"accountId")
    dropdown=Select(ddm)
    ddown=dropdown.options
    print("DDM options are:")
    for x in (ddown):
        print(x.text)
    #print(dropdown.all_selected_options)
    time.sleep(2)
    length=len(ddown)
    print(length,"options are displayed in the DDM")
    first_inlist=dropdown.first_selected_option

    print("First option in the DDM listed is:",first_inlist.text)
    fourth_option=ddown[4].text
    if(fourth_option=='Credit Card'):
        print("Credit Card is displayed 4th in the list")
    else:
        print("Credit Card not found in the list.")