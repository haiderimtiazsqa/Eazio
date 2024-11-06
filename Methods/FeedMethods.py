import os
from lib2to3.fixes.fix_input import context

import pyautogui
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from Eazio.Elements.FeedElements import *


def click_discover_tab(context):
        discover_tab = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Feed.DiscoverTab))
        )
        discover_tab.click()

def click_media_section(context):
        media_section = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Feed.ClickMedia))
        )
        media_section.click()


def enter_feed_description(context, description):
        description_field = WebDriverWait(context.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, Feed.FeedDescription))
        )
        description_field.clear()
        description_field.send_keys(description)

def upload_image(context, image_name="test.jpg"):
    # Construct the full path to the image file in the "media" folder within the project
    media_folder = os.path.join(os.getcwd(), 'media')
    image_path = os.path.join(media_folder, image_name)

    # Click the button using the provided XPath
    upload_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/app-root/app-discover/div/div[2]/div[2]/app-create-post/div[2]/div[2]/div/div/div[1]/div/div[2]/div[6]/div/button/img"))
    )
    upload_button.click()

    # Locate the file input field (typically visible after clicking the button) and send the file path to it
    file_input = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    file_input.send_keys(image_path)

# @when(u'the admin uploads any relevant media')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: When the admin uploads any relevant media')



def click_add_post_button(context):
        add_post_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Feed.Addpost))
        )
        add_post_button.click()
        time.sleep(5)


def click_like(context):
    # Wait until the "Like" button is clickable
    like_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Feed.Likes))
    )

    # Click the "Like" button
    like_button.click()

    # Optional: Wait to allow UI changes after the click
    time.sleep(3)


def add_comment(context, comment_text):
    # Locate the comment input field and enter the comment text
    comment_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Feed.Comment))
    )
    comment_input.clear()
    comment_input.send_keys(comment_text)

    # Locate and click the "Comment" button to submit the comment
    comment_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Feed.Commnet_button))
    )
    comment_button.click()

    # Optional: Wait to ensure the comment is posted
    time.sleep(3)


# Method to redirect to the "All Event" section
def redirect_to_all_event(context):
    all_event_tab = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Feed.All_Event_tab))
    )
    all_event_tab.click()
    time.sleep(3)

def click_add_event_button(context):
    event_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, Feed.Event_button))
    )
    event_button.click()
    time.sleep(3)

def add_event(context, event_title="Sample Event Title"):
    event_title_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Feed.Event_title))
    )
    event_title_input.clear()
    event_title_input.send_keys(event_title)


def add_event(context):
    event_title = "Sample Event Title"
    # Enter the event title
    event_title_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Feed.Event_title))
    )
    event_title_input.clear()
    event_title_input.send_keys(event_title)
    time.sleep(3)

    # Select the start date
    start_date_input = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, Feed.Event_start_date_picker))
    )
    start_date_input.click()  # Open the date picker
    time.sleep(5)

def select_date_using_shadow_dom(context, target_date="1732042800000"):
    try:
        # Locate the shadow host element using JavaScript
        shadow_host = WebDriverWait(context.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'shadow-host-selector'))  # Replace with actual selector
        )
        shadow_root = context.driver.execute_script('return arguments[0].shadowRoot', shadow_host)

        # Locate and click on the date inside the shadow DOM
        day_element = WebDriverWait(shadow_root, 20).until(
            EC.element_to_be_clickable((By.XPATH, f"//div[@class='day unit' and @data-time='{target_date}']"))
        )
        day_element.click()
        print(f"Successfully selected date: {target_date}")
    except Exception as e:
        print(f"Failed to select date. Error: {str(e)}")
        raise
