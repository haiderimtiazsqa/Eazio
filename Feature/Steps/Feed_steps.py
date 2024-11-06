import string
import time
from random import random

from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Eazio.Methods.AddScheduleMethods import *
from Eazio.Methods.FeedMethods import *
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





@when(u'the admin navigates to the "Feeds" section')
def step_impl(context):
    click_discover_tab(context)
@when(u'the admin clicks on "Create Feed"')
def step_impl(context):
    click_media_section(context)

@when(u'the admin enters the feed content')
def step_impl(context):
    description = "This is a sample feed description."  # Replace with desired content
    enter_feed_description(context, description)
    time.sleep(5)

    # upload_image(context)


@when(u'the admin clicks the "Post" button')
def step_impl(context):
    click_add_post_button(context)


# @then(u'the new feed should be visible in the "Feeds" section')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then the new feed should be visible in the "Feeds" section')

@when(u'the admin clicks on "Like" for the newly created feed')
def step_impl(context):
    click_like(context)

@when(u'the admin write comment on feed')
def step_impl(context):
    # Assuming the feed content is stored in context, or fetch dynamically
    comment_text = "This is a sample comment."

    # Call the add_comment function from your code
    add_comment(context, comment_text)



@when(u'the admin redirect to all event')
def step_impl(context):
    redirect_to_all_event(context)



@when(u'the admin click on add event button')
def step_impl(context):
    click_add_event_button(context)


@when(u'admin add the event')
def step_impl(context):
    add_event(context)
    select_date_using_shadow_dom(context)


