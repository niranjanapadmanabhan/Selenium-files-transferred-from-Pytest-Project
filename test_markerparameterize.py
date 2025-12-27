import pytest
from selenium import webdriver


#Data driven example- Creating array named username with values. This function will run 4 times because we have 4 values.
@pytest.mark.parametrize("username",["","1234","abc","admina"])
def test_username(username):
    print("My username is:",username)
    driver = webdriver.Chrome()
    print("open chrome")
    driver.get("https://www.google.com/")
    driver.maximize_window()