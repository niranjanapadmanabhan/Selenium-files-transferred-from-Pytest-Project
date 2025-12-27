import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.mark.parametrize("username,password",[("admin","pass1"),
                                              ("admina","pass2"),
                                              ("!@#$%","po@#A")])
def test_usernamepwd(username,password):
    driver=webdriver.Chrome()
    driver.get("http://ezhrs.com/project1/ezcourses/admin/admin.asp?action=admin")
    # Finding the element for username
    uname = driver.find_element(By.NAME, value="uname")
    # Typing username
    uname.send_keys(username)
    # Finding element for password
    paswd = driver.find_element(By.NAME, value="password")
    # Typing password
    paswd.send_keys(password)
 # Finding element for Login button
    login = driver.find_element(By.NAME, value="SUBMIT")
    # To click the button login
    login.click()
    error=driver.find_element(By.LINK_TEXT,"Try again").text
    print(error)
    if(error=="Try again"):
        print("Test case passed")
    else:
        print("Test case failed")
        driver.find_element(By.LINK_TEXT,"Try again").click()