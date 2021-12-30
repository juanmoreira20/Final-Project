from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import os
import sys

current_dir = os.path.dirname(os.path.realpath(__file__))
path_dir = os.path.join(current_dir, 'json_scenarios')
sys.path.append(path_dir)
from json_utils import *


@given("User is logged in SGME and is currently on documentation webpage")
def given(context):
    context.driver = webdriver.Chrome("C://Users/juan/Documents/chromedriver.exe")
    context.driver.get("webpage")

    username_field = context.driver.find_element(By.ID, "login")
    username_field.send_keys("juan.moreira@dellead.com")

    password_field = context.driver.find_element(By.ID, "inputPassword")
    password_field.send_keys("abcd1234")

    context.driver.find_element(By.ID, "btnLogin").click()

    doc_button = WebDriverWait(context.driver, 100).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/nav/div/div[2]/ul[3]/li[7]/a')))
    doc_button.click()

@when("User use it's credentials to get their respective token and apply for the authorization")
def when(context):
    auth = get_token()
    aut_button = WebDriverWait(context.driver, 100).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-swagger/div/app-custom-card/div/div[2]/div/div/div/div[2]/div[2]/section/div/button')))
    aut_button.click()

    aut_input = WebDriverWait(context.driver, 100).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-swagger/div/app-custom-card/div/div[2]/div/div/div/div[2]/div[2]/section/div/div/div[2]/div/div/div[2]/div/form/div[1]/div/div[4]/section/input')))
    aut_input.send_keys(auth)

    aut_button2 =WebDriverWait(context.driver, 100).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '/html/body/app-root/app-sidebar-layout/div/div/app-swagger/div/app-custom-card/div/div[2]/div/div/div/div[2]/div[2]/section/div/div/div[2]/div/div/div[2]/div/form/div[2]/button[1]')))
    aut_button2.click()


@then("SGME platform informs that the authorization process was successful")
def then(context):
    WebDriverWait(context.driver, 60).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, '//*[@id="swagger-ui"]/div/div[2]/div[2]/section/div/div/div[2]/div/div/div[2]/div/form/div[1]/div/h6')))
