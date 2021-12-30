from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("User is logged in SGME and is currently on SGME webpage")
def given(context):
    context.driver = webdriver.Chrome("C://Users/juan/Documents/chromedriver.exe")
    context.driver.get("webpage")


    username_field = context.driver.find_element(By.ID, "login")
    username_field.send_keys("juan.moreira@dellead.com")

    password_field = context.driver.find_element(By.ID, "inputPassword")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element(By.ID, "btnLogin")
    login_button.click()



@when("User clicks on permission tag in sidebar")
def when(context):
    permissions_button = WebDriverWait(context.driver, 100).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[3]/li[3]/a')))
    permissions_button.click()



@then("SGME platform redirects the user to the permissions page")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="header"]/span[1]/span')))
