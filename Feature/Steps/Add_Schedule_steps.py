import string
import time
from random import random

from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Eazio.Methods.AddScheduleMethods import *
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
from Eazio.Variables.ScheduleVariables import *
from Eazio.Variables.RegistrationVariables import RegistrationVariables
from Eazio.Variables.RegistrationVariables import OnboardingVariables


@given('the user clicks on the schedule tab')
def step_click_schedule_tab(context):
    click_schedule_tab(context)

@given('the user clicks the add schedule button')
def step_click_add_schedule(context):
    click_add_schedule_button(context)

# @when('the user enters the schedule name "{name}"')
# def step_enter_schedule_name(context):
#     enter_schedule_name(context, shcedulevariable.Name)

@when(u'the user enters the schedule name')
def step_impl(context):
    enter_schedule_name(context, shcedulevariable.Name)



@when(u'the user enters the schedule description')
def step_impl(context):
    enter_schedule_description(context, shcedulevariable.Description)

@when(u'the user selects the timings')
def step_impl(context):
    select_schedule_timings(context)
    time.sleep(5)
    select_start_time(context)
    time.sleep(5)
    select_end_time(context)



# @when('the user selects the start time')
# def step_select_start_time(context):
#     select_start_time(context)
#
# @when('the user selects the end time')
# def step_select_end_time(context):
#     select_end_time(context)


@when(u'the user selects the schedule days')
def step_impl(context):
    select_schedule_day(context)


@then('the user clicks on the add button')
def step_click_add_button(context):
    click_add_button(context)

@then('the user should see a success message "{expected_message}"')
def step_verify_success_message(context, expected_message):
    verify_success_message(context, expected_message)
