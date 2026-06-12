
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



#dfincion  para instalar  el  driver

def get_driver():
    service= Service(ChromeDriverManager().install())
    driver= webdriver.Chrome(service=service)
    return driver

def login(driver, user, password):

    wait = WebDriverWait(driver,10)
    driver.get("https://www.saucedemo.com")
    username=wait.until(
        EC.presence_of_element_located((By.ID, "user-name"))
            )
    username.send_keys(user)
    passwrd = wait.until(
        EC.presence_of_element_located((By.ID,"password"))
            )
    passwrd.send_keys(password)

    boton= wait.until(
        EC.element_to_be_clickable((By.ID, "login-button"))
    )

    boton.click()

def titulo(driver):
    Wait= WebDriverWait(driver, 10)
    element = Wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "app_logo"))
    )
    return element.text

def titulo_list(driver):
    Wait= WebDriverWait(driver, 10)
    element = Wait.until(
        EC.presence_of_element_located((By.XPATH,"//span[contains(@data-test,'title')]"))
    )
    return element.text

def lista_de_productos (driver):
    Wait =WebDriverWait(driver,10)
    productos= Wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test="inventory-item"]'))
    )
    return productos

def get_product_title( product):
    # product es  un  'Webelement', aqui  ya  no uso esperas pues  el  elemnto fue  oprtunamente cargado
    return product.find_element(By.CSS_SELECTOR, '[data-test="inventory-item-name"]').text

def get_product_price(product):

    return product.find_element(By.CSS_SELECTOR,'[data-test="inventory-item-price"]').text
