from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

for i in range(5):
    options = Options()
    browser = webdriver.Chrome("C:\webdrivers\chromedriver.exe", options = Options())
    browser.get('https://directpoll.com/v?XDVhEtbsQiP0Cavu05s7Go0oMqX5Z')
    time.sleep(1)
    button = browser.find_element(by = By.XPATH, value = '//*[@id="cont0"]/div/form/div/fieldset/div[2]/div[1]/label')
    button.click()
    button_submit = browser.find_element(by = By.XPATH, value ='//*[@id="cont0"]/div/form/div/fieldset/div[2]/div[5]/input')
    button_submit.click()
    time.sleep(3)
    browser.close()