from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from Elements.LoginElements import LoginElements
from Variables.LoginVariables import LoginVariable


def URL_open(context):
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")  # Start maximized

    # Initialize the Chrome WebDriver
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    # Open the specified URL
    context.driver.get(LoginVariable.application_url)


def enter_email(context, email):
    email_field = context.driver.find_element(By.XPATH, LoginElements.EMAIL_TEXTBOX)
    email_field.clear()  # Clear the field if needed
    email_field.send_keys(email)

def enter_password(context, password):
    password_field = context.driver.find_element(By.XPATH, LoginElements.PASSWORD_TEXTBOX)
    password_field.clear()  # Clear the field if needed
    password_field.send_keys(password)

def click_signin_button(context):
    signin_button = context.driver.find_element(By.XPATH, LoginElements.LOGIN_BUTTON)
    signin_button.click()



