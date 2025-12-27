from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("http://ezhrs.com/project1/ezcourses/admin/admin.asp?action=admin")
driver.maximize_window()
# login
uname = driver.find_element(By.NAME, value="uname")
# Typing username
uname.send_keys("admin")
# Finding element for password
paswd = driver.find_element(By.NAME, value="password")
# Typing password
paswd.send_keys("pass")
# Finding element for Login button
login = driver.find_element(By.NAME, value="SUBMIT")
# To click the button login
login.click()
time.sleep(3)


# click students hyperlink


@pytest.mark.parametrize("f_name,l_name,xpath",
                         [("Ninj", "P",
                           "/html[1]/body[1]/table[2]/tbody[1]/tr[1]/td[1]/table[2]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[1]/td[1]/div[1]/table[3]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[4]/td[1]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/a[1]")])
def test_addstudent(f_name, l_name,xpath):
    driver.find_element(By.LINK_TEXT, "Students").click()
    time.sleep(3)
    # click Add student hyperlink
    driver.find_element(By.LINK_TEXT, "Add Student").click()
    driver.find_element(By.NAME, "fname").clear()
    driver.find_element(By.NAME, "lname").clear()

    #Fill the firstname field
    driver.find_element(By.NAME, "fname").send_keys(f_name)
    firstname = driver.find_element(By.NAME, "fname").get_attribute("value")
    print("First name added is:", firstname)

    # Fill the lastname field
    driver.find_element(By.NAME, "lname").send_keys(l_name)
    lastname = driver.find_element(By.NAME, "lname").get_attribute("value")
    print("Last name added is:", lastname)
    username1 = lastname + " " + firstname  #printing this as reverse coz once student is added it's displayed with lname fname..so to compare with displayed keeping in variable and comparing.
    print("User name added is:", username1)
    # Fill the username field
    driver.find_element(By.NAME, "username").send_keys(username1)
    # Fill the email field
    driver.find_element(By.NAME, "email").send_keys("nir@g.cm")
    # Fill the phone field
    driver.find_element(By.NAME, "phone_code").send_keys("41")
    #Country dropdown
    ddm = Select(driver.find_element(By.XPATH, "//select[@id='CountrySelect']"))
    ddm1 = ddm.select_by_value("Canada")
    time.sleep(5)
    #click the add student button to add the student just created
    driver.find_element(By.NAME, "submit").click()
    time.sleep(5)

    #Will reach Students page showing the list of students
    #driver.refresh()
    displayed = driver.find_element(By.XPATH, "//a[contains(text(),xpath)]").text
    print("Displayed name is:",displayed)
    time.sleep(3)
    # driver.get("http://ezhrs.com/project1/ezcourses/admin/students.asp?action=view")
    #time.sleep(2)
    # # Construct XPath dynamically using the parameterized value
    # displayed_xpath = f"//a[contains()='{fullname}']"
    # displayed_name = driver.find_element(By.XPATH, displayed_xpath).text
    # print("Displayed student list is:", displayed_name)
    #
    if (username1 == displayed):
        print("Test case passed")
    else:
        print("Test case failed")
