from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def before_scenario(context, scenario):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    context.driver.quit()

