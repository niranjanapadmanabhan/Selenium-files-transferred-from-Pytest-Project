import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
# @pytest.yield_fixture()
# #for fixture, no need to give "test_"
# def setup():
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://www.ezhrs.com/project1/potdb/login.asp")
    # username
driver.find_element(By.NAME, "username").send_keys("admin.admin")
    # password
driver.find_element(By.NAME, "password").send_keys("welcome")
    # Click login
driver.find_element(By.NAME, "SUBMIT").click()
    # yield
    # driver.quit()

@pytest.mark.parametrize("username1",["Nir14",
                                      "Nir15"])
def test_create(username1):
    driver.find_element(By.LINK_TEXT,"Create PO").click()
    time.sleep(10)
    #Select PO No. ToRcat
    first_ddm=driver.find_element(By.NAME,"POopco")
    ddm1=Select(first_ddm)
    ddm1.select_by_value("TORcat")
    #Purchased By
    driver.find_element(By.NAME,"Orderedby").send_keys(username1)
    addedname=driver.find_element(By.NAME,"Orderedby").get_attribute("value")
    #Remove the extra space at first to match with the displayed name, otherwise it will say test case failed.
    addedname[1:]
    print("Added requestor name is:",addedname)
    len1 = len(addedname)
    print("Length is:",len1)
    time.sleep(3)
    #Select Catalyst OpCo
    second_ddm = driver.find_element(By.NAME, "OpCo")
    ddm2=Select(second_ddm)
    ddm2.select_by_value("1")
    #Supplier
    third_ddm = driver.find_element(By.NAME, "Supplier")
    ddm3 = Select(third_ddm)
    ddm3.select_by_value("14")
    #Shipping Address
    fourth_ddm = driver.find_element(By.NAME, "shipping")
    ddm4 = Select(fourth_ddm)
    ddm4.select_by_value("1 Dundas Street West, Suite 2800 Toronto Ontario, M5G1Z1")
    # Billing Address
    fifth_ddm = driver.find_element(By.NAME, "billing")
    ddm5 = Select(fifth_ddm)
    ddm5.select_by_value("1 Dundas Street West, Suite 2800 Toronto Ontario, M5G1Z1")
    driver.find_element(By.NAME, "Item1").send_keys("Barrel")
    driver.find_element(By.NAME, "PartNo1").send_keys("AB123")
    driver.find_element(By.NAME, "ModelNo1").send_keys("BRL01")
    driver.find_element(By.NAME, "Quantity1").send_keys("8")
    driver.find_element(By.NAME, "Uprice1").send_keys("80")
    time.sleep(5)  #This step is important as without it, error was showing for the next line as element click not interceptable. So either scroll down fast, or introduce this mandatory sleep statement.
    driver.find_element(By.NAME, "submit").click()
    time.sleep(10)
    displayedname= driver.find_element(By.XPATH, f"//td[contains(text(),'{addedname}')]").text
    print("Displayed name is:",displayedname)
    len2 = len(displayedname)
    print("Length of displayed name is:", len2)
    time.sleep(5)
    if(displayedname==addedname):
        print("Test case passed")
    else:
        print("Test case failed")



