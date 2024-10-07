import string
import time
from random import random

import fake
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Elements.RegistrationElements import RegistrationElements
from Methods.AddEmployeeMethods import generate_random_string
from Variables.RegistrationVariables import RegistrationVariables
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Elements.RegistrationElements import OnboardingElements



def click_get_start_button(context):
    get_start_button = context.driver.find_element(By.XPATH, OnboardingElements.GetStartButton)
    get_start_button.click()


def enter_business_name(context):
    fake = Faker()
    business_name = fake.company()  # Generate a random business name using Faker
    business_name_field = context.driver.find_element(By.XPATH, OnboardingElements.BusinessNameField)
    business_name_field.clear()  # Clear the field if needed
    business_name_field.send_keys(business_name)
    time.sleep(3)  # Optional: Add delay for visibility if necessary

def select_business_category(context):
    # Click on the business category dropdown
    context.driver.find_element(By.XPATH, OnboardingElements.BusinessCategoryClick).click()
    # Select the desired category value
    context.driver.find_element(By.XPATH, OnboardingElements.BusinessCategoryValue).click()

def select_business_type(context):
    # Click on the business type dropdown
    context.driver.find_element(By.XPATH, OnboardingElements.BusinessTypeClick).click()
    # Select the desired type value
    context.driver.find_element(By.XPATH, OnboardingElements.BusinessTypeValue).click()

def enter_phone_number(context, phone_number):
    phone_number_field = context.driver.find_element(By.ID, OnboardingElements.PhoneNumberField)
    phone_number_field.clear()  # Clear the field if needed
    phone_number_field.send_keys(phone_number)

def enter_website(context, website):
    website_field = context.driver.find_element(By.XPATH, OnboardingElements.WebsiteField)
    website_field.clear()  # Clear the field if needed
    website_field.send_keys(website)

def enter_address(context, address):
    address_field = context.driver.find_element(By.XPATH, OnboardingElements.AddressField)
    address_field.clear()  # Clear the field if needed
    address_field.send_keys(address)

def select_country(context):
    # Click on the country dropdown
    context.driver.find_element(By.XPATH, OnboardingElements.CountryField).click()
    # Select the desired country value
    context.driver.find_element(By.XPATH, OnboardingElements.CountryFieldValue).click()

def select_city(context):
    # Click on the city dropdown
    context.driver.find_element(By.XPATH, OnboardingElements.CityField).click()
    # Select the desired city value
    context.driver.find_element(By.XPATH, OnboardingElements.CityValue).click()

def click_verify_button(context):
    verify_button = context.driver.find_element(By.XPATH, OnboardingElements.verifyButton)  # Adjust XPath if necessary
    verify_button.click()


####################=====enter OTP=====############################


