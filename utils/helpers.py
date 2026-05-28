
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import  Service


#dfincion  para instalar  el  driver

def get_driver():
    service= Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service)
    return driver

def login(driver, user, password):
    driver.get("https://www.saucedemo.com")




