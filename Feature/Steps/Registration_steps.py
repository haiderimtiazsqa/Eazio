import string
import time
from random import random

from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

# import Methods.LoginMethods
from Eazio.Methods.LoginMethods import *
from Eazio.Variables.LoginVariables import *
from behave import when, given
from Eazio.Methods.RegistrationMethods import *
from Eazio.Methods.OnboardingMethods import *
from behave import fixture, use_fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

from Eazio.Variables.RegistrationVariables import RegistrationVariables
from Eazio.Variables.RegistrationVariables import OnboardingVariables


@given(u'the user is on the registration page')
def step_impl(context):
    navigate_to_registration_page(context)
    context.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@when(u'the user enters the First Name')
def step_impl(context):
    enter_first_name(context, RegistrationVariables.FirstName)

@when(u'the user enters the Last Name')
def step_impl(context):
    enter_last_name(context, RegistrationVariables.LastName)


@when(u'the user enters the Username')
def step_impl(context):
    generate_random_username(context)


@when(u'the user enters the Email')
def step_impl(context):
    # unique_email = generate_unique_email()
    # enter_email(context, unique_email)
    #
    unique_email = generate_unique_email()
    context.email = unique_email  # Store the unique email in context
    enter_email(context, unique_email)

@when(u'the user enters the Password')
def step_impl(context):
    enter_password(context, RegistrationVariables.Password)

@when(u'the user enters the Confirm Password')
def step_impl(context):
    enter_confirm_password(context, RegistrationVariables.ConfirmPassword)
    # time.sleep(3)

@when(u'the user clicks the next button')
def step_impl(context):
    click_next_button(context)
    time.sleep(3)

@then(u'the user should be taken to the next step of registration')
def step_impl(context):
    # Here you can assert that the next step is displayed or that the URL has changed, etc.
    # assert "https://stg.eazio.com/on-board/business" in context.driver.current_url  # Replace with actual check
    time.sleep(3)

# Second scenerio


@when('the user clicks the get start button')
def step_when_clicks_get_start_button(context):
    click_get_start_button(context)
    time.sleep(3)


@then('the user is redirected to the business information form')
def step_then_redirected_to_business_info_form(context):
    # Wait for the page to load and check for specific text
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-get-started/div/div/div[2]/app-business-info/div/div[2]/p[2]"))
        # Adjust the XPath as necessary
    )

    # Assert that the text is present on the page
    page_source = context.driver.page_source
    assert "Business Information" in page_source, "Business Information text not found on the page."

    print("Successfully navigated to the Business Information form.")

@when('the user enters the business name')
def step_when_enters_business_name(context):
    enter_business_name(context)

@when('the user selects the business category')
def step_when_selects_business_category(context):
    select_business_category(context)

@when('the user selects the business type')
def step_when_selects_business_type(context):
    select_business_type(context)

@when('the user enters the phone number')
def step_when_enters_phone_number(context):
    enter_phone_number(context, OnboardingVariables.PhoneNumber)

@when('the user enters the website')
def step_when_enters_website(context):
    enter_website(context, OnboardingVariables.Website)

@when('the user enters the address')
def step_when_enters_address(context):
    enter_address(context, OnboardingVariables.Address)

@when('the user selects the country')
def step_when_selects_country(context):
    select_country(context)
    time.sleep(5)

@when('the user selects the city')
def step_when_selects_city(context):
    select_city(context)
    time.sleep(10)

@when('the user clicks the verify button')
def step_when_clicks_verify_button(context):
    click_verify_button(context)
    time.sleep(10)

@when(u'the user enters the OTP')
def step_impl(context):
    # if not hasattr(context, 'email'):
    #     raise Exception("Email not found in context. Ensure the email is set before retrieving the OTP.")

    unique_email = context.email  # Retrieve the email from context
    retrieve_otp_and_verify(context, unique_email)  # Retrieve and verify the OTP