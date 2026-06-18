from utils.helpers import login
from utils.helpers import titulo
from utils.helpers import titulo_list
from utils.helpers import lista_de_productos
from utils.helpers import get_product_title
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



    
def test_agregar_al_carrito(driver):

    login(driver,"standard_user", "secret_sauce")

    # vamos  a  verificar   que  existe  el  carrito,  y  que  se actualiza el contador  al   pressionar  le  boton correspondiente
    wait= WebDriverWait(driver, 10)
    elements= driver.find_elements(By.CLASS_NAME,"inventory_item_label")

    #registrolos  ids de los  productos  para   verificar  mas  tarde,  la existencia  en el carrito.
    produt_ids =[]
    for e in elements :
         produt_ids.append((e.find_element(By.CSS_SELECTOR, ":first-child")).get_attribute("id"))
    
    assert len(produt_ids)==6

    btn_add_car= wait.until(
                EC.element_to_be_clickable((By.XPATH,"//Button[ contains(text(),'Add to cart')]"))
                )
    btn_add_car.click()

    # verificamos  que el  carrito cargo incremento  el  elemento  agregado
    cart_badge= driver.find_element(By.CSS_SELECTOR,"[data-test='shopping-cart-link']")
    assert cart_badge.text == '1'    

    # ahora  hacemos  click  y vemos  si nos  lleva  a los  productos del carrito
    cart_badge.click()
    assert driver.current_url == "https://www.saucedemo.com/cart.html", "fallo el redireccionamiento"

    #ahora  vamos  a verificar  que  el elemento agregado a la  carrito  , esta  realmente incluido
    id_element_in_cart= driver.find_element(By.CSS_SELECTOR,".cart_item .cart_item_label > :first-child").get_attribute("id")
    assert id_element_in_cart==produt_ids[0]