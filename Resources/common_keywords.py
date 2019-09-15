# coding=utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import csv
from pathlib import Path

# Variables
base_path = Path(__file__).parent
passwords_path = (base_path / '../Resources/passwords.csv').resolve()
proxy_path = (base_path / '../drivers/chrome_proxy.zip')
chrome_path = (base_path / '../drivers/chromedriver')
firefox_path = '/Users/paragshah/PycharmProjects/intergratedautomationframework/FF_Profile'
output_path = (base_path / '../Reports/')
screenshot_path = (base_path / '../Screenshots/')

# Read data from passwords file
with open(passwords_path) as p:
    for line in csv.reader(p):
        u = line[0]
        p = line[1]

username = u
password = p


# Functions
def launch_browser(url):
    """ Open browser and load url """

    chrome_options = Options()
    chrome_options.add_extension(proxy_path)
    driver = webdriver.Chrome(chrome_path, options=chrome_options)
    print('Browser launched')

    driver.set_page_load_timeout(10)
    driver.get(url)
    driver.maximize_window()
    print('URL loaded')
    return driver


def quit_browser(driver):
    """ Quit browser """

    if driver is not None:
        time.sleep(5)
        driver.quit()
    print('Tests completed')
