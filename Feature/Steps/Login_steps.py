import time

from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

import Methods.LoginMethods
from Methods.LoginMethods import *
from Variables.LoginVariables import *



@given(u'the user is on the login page')
def step_impl(context):
    URL_open(context)
    time.sleep(5)

@when(u'the user enters the username and password')
def step_impl(context):
    enter_email(context, LoginVariable.admin_email)
    enter_password(context, LoginVariable.admin_password)



@when(u'the user clicks the login button')
def step_when_user_clicks_login(context):
    click_signin_button(context)
    time.sleep(5)

@then(u'the user should be redirected to the dashboard')
def step_then_user_redirected(context):
    expected_url = "https://stg.eazio.com/dashboard/admin"  # The expected URL
    assert context.driver.current_url == expected_url, f"Expected URL: {expected_url}, but got: {context.driver.current_url}"
    time.sleep(5)

