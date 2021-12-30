from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@given("User is logged in SGME")
def given(context):
    context.driver = webdriver.Chrome("C://Users/juan/Documents/chromedriver.exe")
    context.driver.get("webpage")


    username_field = context.driver.find_element(By.ID, "login")
    username_field.send_keys("juan.moreira@dellead.com")

    password_field = context.driver.find_element(By.ID, "inputPassword")
    password_field.send_keys("abcd1234")

    login_button = context.driver.find_element(By.ID, "btnLogin")
    login_button.click()

@when("User tries to log out by using the respective button")
def when(context):
    loggout_button = WebDriverWait(context.driver, 100).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-accessibility-bar/div/nav/div/ul/ul/li[2]/button')))
    loggout_button.click()


@then("SGME platform redirects the user to the log in page")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH,
         '/html/body/app-root/app-login/div/div/app-login-form/div[1]/div/div/img')))
