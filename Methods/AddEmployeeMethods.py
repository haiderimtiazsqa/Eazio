import time
from selenium.webdriver.support.ui import Select
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
from Elements.AddemployeeElements import *
from Variables.AddEmployeeVariables import *
import random
import string

# class DashboardActions:
#     @staticmethod
#     def navigate_to_dashboard(driver, url):
#         driver.get(url)  # Navigate to the specified URL
#         assert "Dashboard" in driver.title  # Check if the dashboard is loaded


def click_people_tab(context):
    people_tab = context.driver.find_element(By.XPATH, AddEmployeeElements.PeopleTabsidebar)
    people_tab.click()
    time.sleep(3)

def click_employees_tab(context):
    employee_tab = context.driver.find_element(By.XPATH, AddEmployeeElements.Employeetab)
    employee_tab.click()


def click_add_btn(context):
    try:
        # Wait until the button is visible and clickable
        WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, AddEmployeeElements.AddEmpbutton))
        )
        WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, AddEmployeeElements.AddEmpbutton))
        )

        employee_button = context.driver.find_element(By.XPATH, AddEmployeeElements.AddEmpbutton)
        employee_button.click()
    except Exception as e:
        print(f"Error clicking the Add Employee button: {e}")

def enter_employee_name(context, EmployeeFName):
    employee_name_field = context.driver.find_element(By.XPATH, AddEmployeeElements.EmployeeName)
    employee_name_field.clear()  # Clear the field if needed
    employee_name_field.send_keys(EmployeeFName)

def enter_employee_last_name(context, EmployeeLName):
    employee_last_name_field = context.driver.find_element(By.XPATH, AddEmployeeElements.EmployeeLastName)
    employee_last_name_field.clear()  # Clear the field if needed
    employee_last_name_field.send_keys(EmployeeLName)

# def enter_employee_email(context, EmployeeEmail):
#     employee_email_field = context.driver.find_element(By.XPATH, AddEmployeeElements.EmployeeEmail)
#     employee_email_field.clear()  # Clear the field if needed
#     employee_email_field.send_keys(EmployeeEmail)

def generate_random_string(length=10):
    """Generate a random string of specified length."""
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def generate_unique_email(domain="yopmail.com"):
    """Generate a unique email address using a random string."""
    random_part = generate_random_string()  # Generate a random string
    unique_email = f"{random_part}@{domain}"  # Construct the email address
    return unique_email

def enter_employee_email(context, email):
    employee_email_field = context.driver.find_element(By.XPATH, AddEmployeeElements.EmployeeEmail)
    employee_email_field.clear()  # Clear the field if needed
    employee_email_field.send_keys(email)

def enter_employee_mobile_number(context, mobile_number):
    mobile_number_field = context.driver.find_element(By.XPATH, AddEmployeeElements.Employeenumber)
    mobile_number_field.clear()  # Clear the field if needed
    mobile_number_field.send_keys(mobile_number)


def select_manager(context):
    # Click on the dropdown to open it
    manager_dropdown = context.driver.find_element(By.XPATH, AddEmployeeElements.EmployeeManagerDropdown)
    manager_dropdown.click()

    # Create a Select object
    select = Select(manager_dropdown)

    # Select the desired option by its value
    select.select_by_value("9431052b-460c-4fed-82d4-702aadd61dfb")  # Selecting 'own admin'

    # Click again to confirm the selection (if needed)
    confirm_selection = context.driver.find_element(By.XPATH, AddEmployeeElements.EmployeeManagerDropdown)
    confirm_selection.click()  # Click to confirm the selection if necessary
    time.sleep(3)


def select_country(context):
    # Click on the country dropdown to open it
    country_dropdown = context.driver.find_element(By.XPATH, AddEmployeeElements.Employeecountrydropdown)
    country_dropdown.click()

    # # Wait for the country options to load (optional, depending on your application)
    # WebDriverWait(context.driver, 10).until(
    #     EC.presence_of_element_located((By.XPATH, "//li[contains(@class, 'ng-star-inserted')]"))
    # )
    # Select the first country option
    first_country_option = context.driver.find_element(By.XPATH, AddEmployeeElements.Employeecountryvalue)
    time.sleep(3)
    first_country_option.click()  # Click to select the first country


def select_state(context):
    # Click on the city dropdown to open it
    city_dropdown = context.driver.find_element(By.XPATH, AddEmployeeElements.Employeecitydropdown)
    city_dropdown.click()

    # Select the desired city option (e.g., the third option in the list)
    city_option = context.driver.find_element(By.XPATH, AddEmployeeElements.Employeecityvalue)
    city_option.click()  # Click to select the specified city
    time.sleep(3)

def employee_add_btn(context):
    employee_button = context.driver.find_element(By.XPATH, AddEmployeeElements.Addemployeeformbtn)
    employee_button.click()
    time.sleep(5)


