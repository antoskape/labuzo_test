#!/usr/bin/env python3.8

"""
Automated login to Gmail box

Description:
    Automated login to Google mail box with using Selenium library and Chrome browser.
    Undetected_chromedriver is used to avoid "insecure" blocking process (must be as
    first import!).
Originator:
    Peter Antoska
Release:
    01
Date:
    08.09.2022
"""

import undetected_chromedriver as uc
from time import sleep
from selenium.webdriver.common.by import By
import json

if __name__ == "__main__":
    # Read credentials data from file
    with open("credentials.json", "r") as cfile:
        data = cfile.read()
    # Parse JSON
    obj = json.loads(data)

    driver = uc.Chrome()
    # Open Login panel
    driver.get("https://accounts.google.com/")

    # Fill in the email address
    driver.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys(str(obj["user"]))
    # Click on Next-button
    driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button/span').click()
    sleep(3)
    # Fill in the password
    driver.find_element(
        By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input'
    ).send_keys(str(obj["passwd"]))
    # Click on Next button
    driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/span').click()
    sleep(10)

    # Login process was successful
    print("You are logged into Google email account!")
