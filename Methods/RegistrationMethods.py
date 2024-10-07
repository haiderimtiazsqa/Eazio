import string
import time
from random import random

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


def navigate_to_registration_page(context):
    # context.driver.get(RegistrationVariables.RegistrationURL)
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized

    # Initialize the Chrome WebDriver
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # Open the specified URL
    context.driver.get(RegistrationVariables.RegistrationURL)
def enter_first_name(context, first_name):
    first_name_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, RegistrationElements.FirstNameField))
    )
    first_name_field.clear()
    first_name_field.send_keys(first_name)

def enter_last_name(context, last_name):
    last_name_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, RegistrationElements.LastNameField))
    )
    last_name_field.clear()
    last_name_field.send_keys(last_name)

def generate_random_username(context):
    fake = Faker()
    username = fake.user_name()

    # Enter the generated username into the Username field
    username_field = context.driver.find_element(By.XPATH, RegistrationElements.UsernameField)
    username_field.clear()  # Clear the field if needed
    username_field.send_keys(username)
    time.sleep(3)
def generate_unique_email(domain="yopmail.com"):
    """Generate a unique email address using a random string."""
    random_part = generate_random_string()  # Generate a random string
    unique_email = f"{random_part}@{domain}"  # Construct the email address
    return unique_email


def enter_email(context, email):
    email_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, RegistrationElements.EmailField))
    )
    email_field.clear()
    email_field.send_keys(email)




def enter_password(context, password):
    password_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, RegistrationElements.PasswordField))
    )
    password_field.clear()
    password_field.send_keys(password)

def enter_confirm_password(context, confirm_password):
    confirm_password_field = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, RegistrationElements.ConfirmPasswordField))
    )
    confirm_password_field.clear()
    confirm_password_field.send_keys(confirm_password)
    time.sleep(3)

def click_next_button(context):
    next_button = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, RegistrationElements.NextButton))
    )
    next_button.click()
    time.sleep(5)
