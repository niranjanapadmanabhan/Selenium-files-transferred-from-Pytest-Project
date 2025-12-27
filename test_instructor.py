import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


@pytest.mark.parametrize("finame,laname,email2", [("aaa", "bbb", "a1aa.bbbb@gmail.com"),
                                               ("ggg", "jjj", "g1g.jjj@gmail.com"),
                                               ("nnn", "ppp", "n1nn.pppp@gmail.com")])
def test_addinstructor(finame,laname,email2):
    driver = webdriver.Chrome()
    driver.get("http://ezhrs.com/project1/ezcourses/admin/admin.asp?action=admin")
    driver.maximize_window()
    #Finding the element for username
    username = driver.find_element(By.NAME, value="uname")
    #Typing admin for username
    username.send_keys("admin")

    #Finding element for password
    password = driver.find_element(By.NAME, value="password")
    #Typing pass for password
    password.send_keys("pass")

    #Finding element for Login button
    login = driver.find_element(By.NAME, value="SUBMIT")
    #To click the button login
    login.click()

    #Click Instructor
    instructor = driver.find_element(By.LINK_TEXT, value="Instructors")
    instructor.click()

    time.sleep(3)

    #Add Instructor
    addinstructor = driver.find_element(By.LINK_TEXT, value="Add")
    addinstructor.click()
    time.sleep(4)

    #Fill the form
    fname = driver.find_element(By.NAME, value="fname")
    fname.send_keys(finame)
    firstname = driver.find_element(By.NAME, value="fname").get_attribute("value")
    print("First name is:", firstname)
    lastname = driver.find_element(By.NAME, value="lname")
    lastname.send_keys(laname)
    abc = driver.find_element(By.NAME, value="lname").get_attribute("value")
    print("Last name is:", abc)
    time.sleep(4)
    fullname = firstname + " " + abc
    print("Full name is:", fullname)
    uname = driver.find_element(By.NAME, value="username")
    uname.send_keys("Niraj")
    email1 = driver.find_element(By.NAME, value="email")
    email1.send_keys(email2)
    time.sleep(4)
    tel = driver.find_element(By.NAME, value="phone_code")
    tel.send_keys("4165702899")
    time.sleep(4)
    #Click Add Instructor Button
    buttonclick = driver.find_element(By.NAME, value="submit")
    buttonclick.click()
    time.sleep(4)
    actual_fullname = driver.find_element(By.XPATH, f"//div[contains(text(), '{fullname}')]").text #here fullname is the variable we used to store fname+lname
    print("Displayed full name is:", actual_fullname)
    if (fullname == actual_fullname):
        print("Testcase passed")
    else:
        print("Failed")
