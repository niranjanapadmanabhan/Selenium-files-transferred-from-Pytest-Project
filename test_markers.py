import pytest
from selenium import webdriver

#skips this function when we run this entire file.
@pytest.mark.smoke
def test_12():
    print("i love qa")

@pytest.mark.smoke1
def test_13():
    print("i love automation")

@pytest.mark.usefixtures
def test_14():
    driver = webdriver.Chrome()
    print("open chrome")
    driver.get("https://www.google.com/")
    driver.maximize_window()