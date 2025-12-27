import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

#login for PO database

@pytest.mark.parametrize("username,password",[("!@#$.admin","welcome"),
                                              ("12345","welcome"),
                                              ("admin.admin","!@#$%"),
                                              ("ADMIN.ADMIN","12345")])
def test_username(username,password):
    driver = webdriver.Chrome()
    driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
    # username
    driver.find_element(By.NAME, "username").send_keys(username)
    # password
    driver.find_element(By.NAME, "password").send_keys(password)
    # Click login
    driver.find_element(By.NAME, "SUBMIT").click()
    error=driver.find_element(By.LINK_TEXT,"here").text
    print(error)
    if(error=="here"):
        print("Test case passed")
    else:
        print("Test case failed")
    driver.find_element(By.LINK_TEXT,"here").click()
    driver.quit()