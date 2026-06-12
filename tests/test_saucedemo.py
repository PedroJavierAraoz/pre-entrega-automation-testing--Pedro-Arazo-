from utils.helpers import login
from utils.helpers import titulo
from utils.helpers import titulo_list
from utils.helpers import lista_de_productos
from utils.helpers  import get_product_title
from utils.helpers import get_product_price
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


def test_login(driver):

    login(driver,"standard_user", "secret_sauce")
    # Verificamos que la URL cambió a la página de inventario 
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "fallo el login"
    assert titulo(driver) == "Swag Labs", " No se  encontro  el titulo "
    assert titulo_list(driver) == "Products", " No se  encontro  el titulo "

def test_navegacion_productos(driver ):
    #validaremos presencia de productos, lista y nombre  precio 
    #Primero nos logueamos nuevamente  para  poder  acceder  al catalogo de productos
    login(driver,"standard_user", "secret_sauce")
    productos= lista_de_productos(driver)
    #test lista no vaci,  se  encuemtran elementos  
    assert len(productos)>0
    # verificamos  el  titulo del primero
    product_title= get_product_title(productos[0])
    assert product_title =="Sauce Labs Backpack"
    #y ahora  verificamos el precio
    product_price= get_product_price(productos[0])
    assert product_price =="$29.99"
    
    # en estas  dos  lineas verificamos  implicitamente   que  existe  el menu  de  hamburguesa
    menu = driver.find_element(By.ID, "react-burger-menu-btn")
    menu.click()
    #si llegamos  hasta  aca ,  es pq  existe  y no hace  falta  ningun tipo de assert

    wait=WebDriverWait(driver, 5)

    #voy a  verificar  que  el  menu emergente  tiene  elemntos visibles, como  el loink 'about', 
    about_link = wait.until(
        EC.visibility_of_element_located((By.ID, "about_sidebar_link"))
    )
    assert about_link.is_displayed(), "Opción de about no encontrada"
    #ahora  probamos 'reset'
     

    reset_link =   wait.until(
             EC.visibility_of_element_located((By.ID, "reset_sidebar_link"))
    )
    assert reset_link.is_displayed(), "Opción de about no encontrada"
    



