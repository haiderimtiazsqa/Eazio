import string
import time
from random import random

import fake
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Eazio.Elements.RegistrationElements import RegistrationElements
from Eazio.Methods.AddEmployeeMethods import generate_random_string
from Eazio.Variables.RegistrationVariables import RegistrationVariables
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Eazio.Elements.RegistrationElements import OnboardingElements



def click_get_start_button(context):
    get_start_button = context.driver.find_element(By.XPATH, OnboardingElements.GetStartButton)
    get_start_button.click()


def enter_business_name(context):
    fake = Faker()
    business_name = fake.company()  # Generate a random business name using Faker
    business_name_field = context.driver.find_element(By.XPATH, OnboardingElements.BusinessNameField)
    business_name_field.clear()  # Clear the field if needed
    business_name_field.send_keys(business_name)
    time.sleep(5)  # Optional: Add delay for visibility if necessary

def select_business_category(context):
    # # Click on the business category dropdown
    # context.driver.find_element(By.XPATH, OnboardingElements.BusinessCategoryClick).click()
    # time.sleep(5)
    # # Select the desired category value
    # context.driver.find_element(By.XPATH, OnboardingElements.BusinessCategoryValue).click()
    # Click on the business category dropdown
    context.driver.find_element(By.XPATH, OnboardingElements.BusinessCategoryClick).click()

    wait = WebDriverWait(context.driver, 10)  # Set a timeout of 10 seconds

    # Wait for the list of category options to be visible
    options = wait.until(
        EC.visibility_of_all_elements_located((By.XPATH, "//li[contains(@class, 'ng-star-inserted')]"))
    )

    # Find the desired option by its text
    for option in options:
        if option.text == "Trade":  # Match the desired category name
            option.click()  # Click the matching option
            break
    # else:
    #     print(f"Category '{category_name}' not found in the dropdown.")

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
    # # Click on the country dropdown
    # context.driver.find_element(By.XPATH, OnboardingElements.CountryField).click()
    # time.sleep(5)
    # # Select the desired country value
    # context.driver.find_element(By.XPATH, OnboardingElements.CountryFieldValue).click()

    context.driver.find_element(By.XPATH, OnboardingElements.CountryField).click()

    wait = WebDriverWait(context.driver, 10)  # Set a timeout of 10 seconds

    # Wait for the list of country options to be visible
    options = wait.until(
        EC.visibility_of_all_elements_located((By.XPATH, "//li[contains(@class, 'ng-star-inserted')]"))
    )

    # Find the desired country by its text
    for option in options:
        if option.text == "Afghanistan":  # Match the desired country name
            option.click()  # Click the matching option
            break

def select_city(context):
    context.driver.find_element(By.XPATH, OnboardingElements.CityField).click()

    # Attempt to find the list of city options immediately
    options = context.driver.find_elements(By.XPATH, "//li[contains(@class, 'ng-star-inserted')]")

    # Check if options are present
    if options:
        # Find and click the desired city by its text
        for option in options:
            if option.text == "Aībak":  # Match the desired city name
                option.click()  # Click the matching option
                break

def click_verify_button(context):
    wait = WebDriverWait(context.driver, 30)

    verify_button = wait.until(
        EC.visibility_of_element_located((By.XPATH, OnboardingElements.verifyButton))
    )

    # Scroll the button into view
    context.driver.execute_script("arguments[0].scrollIntoView(true);", verify_button)

    # Use JavaScript to click the button
    context.driver.execute_script("arguments[0].click();", verify_button)

####################=====enter OTP=====############################


def retrieve_otp_and_verify(context, yopmail_email):
    # Open Yopmail in a new tab
    context.driver.execute_script("window.open('https://yopmail.com', '_blank');")
    context.driver.switch_to.window(context.driver.window_handles[1])  # Switch to the new tab

    # Wait for the Yopmail page to load
    WebDriverWait(context.driver, 10).until(EC.presence_of_element_located((By.ID, "login")))

    # Enter the email address
    driver = context.driver
    driver.find_element(By.ID, "login").send_keys(yopmail_email)
    time.sleep(5)

    # Click the "Check Inbox" button
    driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/main/div[3]/div/div[1]/div[2]/div/div/form/div/div[1]/div[4]/button/i").click()
    time.sleep(5)

    # Wait for the inbox to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'mail')]")))

    # Locate and click the OTP email (adjust the selector as needed)
    otp_email = driver.find_element(By.XPATH, "//div[contains(@class, 'mail')]")
    otp_email.click()

    # Wait for the email content to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'mail')]")))

    # Extract the OTP from the email content
    otp_message = driver.find_element(By.XPATH, "//div[contains(@id, 'mail')]").text
    otp = otp_message.split(" ")[-1]  # Adjust this logic based on your email format

    print(f"OTP extracted: {otp}")

    # Close the Yopmail tab
    driver.close()  # Close the Yopmail tab
    context.driver.switch_to.window(context.driver.window_handles[0])  # Switch back to the original tab

    # Enter the OTP in your application
    otp_input_xpath = RegistrationElements.OtpInputField  # Adjust this to your actual OTP input field XPath
    otp_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, otp_input_xpath))
    )
    otp_input.clear()  # Clear the field if necessary
    otp_input.send_keys(otp)  # Enter the OTP into the field





