import time
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import Eazio.Methods.LoginMethods
from Eazio.Methods.LoginMethods import *
from Eazio.Variables.LoginVariables import *
from Eazio.Methods.AddEmployeeMethods import *
from Eazio.Variables.AddEmployeeVariables import *
from behave import fixture, use_fixture
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@when('the admin clicks on the People tab from the sidebar')
def step_when_clicks_people_tab(context):
    click_people_tab(context)
    time.sleep(3)


@then(u'the admin should be redirected to the People Insight page')
def step_impl(context):
    expected_url = "https://stg.eazio.com/people"  # The expected URL
    assert context.driver.current_url == expected_url, f"Expected URL: {expected_url}, but got: {context.driver.current_url}"
    time.sleep(3)

@when('the admin clicks on the Employee tab')
def step_when_clicks_employee_tab(context):
    click_employees_tab(context)  # Implement this function in your methods
    time.sleep(5)

@when(u'the admin clicks on the Add Employee button')
def step_impl(context):
    click_add_btn(context)
    time.sleep(5)

@then('the admin should be redirected to the Add Employee form')
def step_then_redirected_to_add_employee_form(context):
    # Verify that the expected text is present on the page
    expected_text = "Add Employee"  # Replace with the actual text you expect
    body_text = context.driver.find_element(By.TAG_NAME, "body").text
    assert expected_text in body_text, f"Expected text '{expected_text}' not found on the page."
    time.sleep(5)

@when('the admin enters the employee\'s first name')
def step_when_enters_first_name(context):
    enter_employee_name(context, AddEmployeeVariables.EmployeeFName)
    time.sleep(2)

@when('the admin enters the employee\'s last name')
def step_when_enters_last_name(context):
    enter_employee_last_name(context, AddEmployeeVariables.EmployeeLName)
    time.sleep(2)

@when('the admin enters the employee\'s email address')
def step_when_enters_email(context):
    unique_email = generate_unique_email()  # Generate a unique email
    enter_employee_email(context, unique_email)  # Use the unique email
    time.sleep(2)
@when('the admin enters the employee\'s mobile number')
def step_when_enters_mobile_number(context):
    enter_employee_mobile_number(context, AddEmployeeVariables.EmployeeNumber)
    time.sleep(2)

@when('the admin selects the reporting manager')
def step_when_selects_reporting_manager(context):
    select_manager(context)

@when('the admin selects the country')
def step_when_selects_country(context):
    select_country(context)

@when('the admin selects the state')
def step_when_selects_state(context):
    select_state(context)

@when('the admin clicks on the Add Employee from button')
def step_when_clicks_add_employee_form_button(context):
    employee_add_btn(context)

@then('the admin should be redirected to the Employee Listing page')
def step_then_redirected_to_employee_listing(context):
    assert "Employee Listing" in context.driver.title, "Title does not contain 'Employee Listing'"  # Verify redirection
    assert context.driver.find_element(By.XPATH, "/html/body/app-root/app-people/div[1]/div[2]/div/div[2]/div[1]/div[1]/p[1]"), "Text 'Employee Information' not found on the page"


