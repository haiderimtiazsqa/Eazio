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

from Eazio.Elements.LoginElements import LoginElements
from Eazio.Variables.LoginVariables import LoginVariable
from Eazio.Elements.AddemployeeElements import *
from Eazio.Variables.AddEmployeeVariables import *
import random
import string
from Eazio.Elements.AddScheduleElements import *



def click_schedule_tab(context):
    people_tab = context.driver.find_element(By.XPATH, AddScheduleElements.ScheduleTab)
    people_tab.click()
    time.sleep(10)

def click_add_schedule_button(context):
    add_schedule_button = context.driver.find_element(By.ID, AddScheduleElements.AddScheduleButton)
    add_schedule_button.click()
    time.sleep(5)

def enter_schedule_name(context, name):
    schedule_name_field = context.driver.find_element(By.ID, AddScheduleElements.ScheduleName)
    schedule_name_field.clear()  # Clear the field if needed
    schedule_name_field.send_keys(name)

def enter_schedule_description(context, description):
    schedule_desc_field = context.driver.find_element(By.ID, AddScheduleElements.ScheduleDescription)
    schedule_desc_field.clear()  # Clear the field if needed
    schedule_desc_field.send_keys(description)
    time.sleep(5)

def select_schedule_timings(context):
    timing_button = context.driver.find_element(By.XPATH, AddScheduleElements.ScheduleTimingClick)
    timing_button.click()
    time.sleep(5)
    timing_field = context.driver.find_element(By.XPATH, AddScheduleElements.clicktimingfield)
    timing_field.click()
    time.sleep(5)

def select_start_time(context):
    start_time = context.driver.find_element(By.XPATH, AddScheduleElements.ScheduleStartTime)
    start_time.click()
    time.sleep(5)
    start_time_ok = context.driver.find_element(By.XPATH, AddScheduleElements.ScheduleStartTimeOkButton)
    start_time_ok.click()
    time.sleep(5)

def select_end_time(context):
    end_time = context.driver.find_element(By.XPATH, AddScheduleElements.ScheduleEndTime)
    end_time.click()
    time.sleep(5)
    end_time_pm = context.driver.find_element(By.XPATH, AddScheduleElements.SelectEndPM)
    end_time_pm.click()
    time.sleep(5)
    end_time_ok = context.driver.find_element(By.XPATH, AddScheduleElements.ScheduleEndTimeOkButton)
    end_time_ok.click()
    time.sleep(5)

# def select_schedule_day(context):
#     shift = context.driver.find_element(By.XPATH, AddScheduleElements.daysetting_click)
#     shift.click()
#     time.sleep(5)
#     all_checkbox = context.driver.find_element(By.ID, AddScheduleElements.All_checkBox)
#     all_checkbox.click()
#     time.sleep(3)

def select_schedule_day(context):
    shift = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, AddScheduleElements.daysetting_click))
    )
    shift.click()
    time.sleep(3)
    # Wait for the All checkbox to be visible and then click it
    all_checkbox = WebDriverWait(context.driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, AddScheduleElements.All_checkBox))
    )
    all_checkbox.click()
    time.sleep(3)



def click_add_button(context):
    add_button = context.driver.find_element(By.XPATH, AddScheduleElements.AddButton)
    add_button.click()
    time.sleep(5)

# def verify_success_message(context, expected_message):
#     success_message = context.driver.find_element(By.XPATH, "//div[contains(text(), 'Schedule added successfully')]")
#     assert expected_message in success_message.text, "Success message not displayed."
