# import time
# from behave import given, when, then
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# import Methods.LoginMethods
# from Eazio.Methods.LoginMethods import *
# from Eazio.Variables.LoginVariables import *
# from Eazio.Methods.AddEmployeeMethods import *
# from Eazio.Variables.AddEmployeeVariables import *
# from behave import fixture, use_fixture
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from webdriver_manager.chrome import ChromeDriverManager
#
#
# @given('the admin is on the dashboard')
# def step_impl(context):
#     """Assuming the admin is already logged in and on the dashboard."""
#     # You could add the login method here if not already logged in
#     pass
#
# @when('the admin clicks on the People tab from the sidebar')
# def step_impl(context):
#     click_people_tab(context)
#
# @when('the admin clicks on the Employee tab')
# def step_impl(context):
#     click_employee_tab(context)
#
# @when('the admin clicks on the latest employee to view details')
# def step_impl(context):
#     click_latest_employee(context)
#
# @then('the admin should see the employee\'s details on the Employee Detail page')
# def step_impl(context):
#     wait_for_employee_detail(context)
#     validate_employee_details_displayed(context)
#
# def click_people_tab(context):
#     """Click on the People tab from the sidebar."""
#     people_tab = context.driver.find_element(By.XPATH, AddEmployeeElements.PeopleTabSidebar)
#     people_tab.click()
#     time.sleep(3)  # Replace with WebDriverWait if possible
#
# def click_employee_tab(context):
#     """Click on the Employee tab."""
#     employee_tab = context.driver.find_element(By.XPATH, AddEmployeeElements.EmployeeTab)
#     employee_tab.click()
#     time.sleep(3)  # Replace with WebDriverWait if possible
#
# def click_latest_employee(context):
#     """Click on the latest employee to view details."""
#     latest_employee_row = context.driver.find_elements(By.XPATH, AddEmployeeElements.EmployeeTableRow)[1]  # Skip header row
#     detail_button = latest_employee_row.find_element(By.XPATH, AddEmployeeElements.DetailButton)
#     detail_button.click()
#     time.sleep(3)  # Replace with WebDriverWait if possible
