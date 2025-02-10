#!/usr/bin/env python3

## Notes:
# Requires selenium
# Username and password should be passed in on command line

# Improvements
# I would wrap a lot of the functions in retry logic. You can use generic function that
# takes the worker function to make it systematic

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest 
import random
import time
import traceback


@pytest.fixture
def driver():
    return webdriver.Chrome()

# Just does the navigation
def navigate(driver: webdriver, location: str):
    driver.get(location)

def wait_for_presence(driver: webdriver, locator:str, waittime:int =10):
    return WebDriverWait(driver, waittime).until(EC.presence_of_element_located(locator))

# Fixture that signs in for the user at the posit cloud site
@pytest.fixture
def sign_in_posit(driver: webdriver, username: str, password: str):

   navigate(driver, "https://posit.cloud")
   wait_for_presence(driver, locator=(By.XPATH, "//a[contains(@href, 'login')]")).click()

   element = wait_for_presence(driver, locator=(By.XPATH, "//input[contains(@name, 'email')]"))
   element.send_keys(username)

   element = wait_for_presence(driver, locator=(By.XPATH, "//button[.='Continue']"))
   element.click()


   element = wait_for_presence(driver, locator=(By.XPATH, "//input[contains(@name, 'password')]"))
   element.send_keys(password)
   element = wait_for_presence(driver, locator=(By.XPATH, "//button[.='Log in']"))
   element.click()

# Verifies we're on the posit cloud main page
def verify_posit_main(driver: webdriver):
  # Uses side effect of checking for presence
  element = wait_for_presence(driver, locator=(By.CSS_SELECTOR, ".productLogo"))

# Automated this before I realized I only got one workspace for posit cloud.
# Might be useful later though...
def create_workspace(driver: webdriver):
  # Cleanup  # Cleanup??
  print("Create Workspace")
  element = wait_for_presence(driver, locator=(By.CSS_SELECTOR, ".newSpace"))
  element.click()
  ran_int = random.randint(1,1000)
  space_name = f"create_project_test_{ran_int}"
  
  
  element = wait_for_presence(driver, locator=(By.XPATH, "//input[@id='name']"))
  element.send_keys(space_name)
  element = wait_for_presence(driver, locator=(By.XPATH, "//button[@type='submit' and contains(., 'Create')]"))
  element.click()
  print("Workspace Created")
  return space_name

# Creates a new project
def create_new_project(driver: webdriver):
   time.sleep(5) # Don't like this, but seems the menu needs some time to stabilise.
   element = wait_for_presence(driver, locator=(By.XPATH, "//button[@title='New Project']"))
   element.click()

   element = wait_for_presence(driver, locator=(By.CSS_SELECTOR, "button.newRStudioProject"))
   element.click()

# Verify that RStudio is loaded.
# Can take some time, so we do some retries.
def verify_rstudio(driver: webdriver, retries:int =10):
   # Rstudio is in an iframe within an iframe, so we need to talk to the right
   # iframe first
   time.sleep(30) # Give the UI a little time to stabilise 
   for _ in range(retries):
     try:
       print("Getting Content iframe")
       content_iframe = wait_for_presence(driver, locator=(By.XPATH, "//iframe[@id='contentIFrame']"), waittime=30)
       print("Switching to content iframe")
       driver.switch_to.frame(content_iframe)
       print("Find help element")
       wait_for_presence(driver, locator=(By.XPATH, "//span[@id='rstudio_label_help_menu']"), waittime=20)
       break
     except Exception as e:
         print("Can't find rstudio, retrying")
         traceback.print_exc(e)
   driver.switch_to.default_content()

# Tests we can sign in, navigate to posit cloud, create a project and RStudio is loaded.
def test_verify_studio(driver: webdriver, username:str, password:str, sign_in_posit):
   # Make sure we navigated correctly.
   verify_posit_main(driver)
   create_new_project(driver)
   verify_rstudio(driver)
   print("Success!!!")
