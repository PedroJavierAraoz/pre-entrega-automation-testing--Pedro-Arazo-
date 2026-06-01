from utils.helpers import login
import pytest


def test_login(driver):

    login(driver,"standard_user", "secret_sauce")
    # Verificamos que la URL cambió a la página de inventario 
    assert driver.current_url == "https://www.saucedemo.c/inventory.html", "fallo el login"
""" 
def test_login(driver):
    login(driver, "standard_user", "secret_sauce")
    # Verificamos que la URL cambió a la página de inventario 
    assert driver.current_url == "https://www.saucedemo.com/inventory.html" """


# def test_login_invalid_credentials(driver):
#     login(driver, "invalid_user", "invalid_password")
#     assert "error" in driver.page_source.lower()


# def test_page_title_after_login(driver):
#     login(driver, "standard_user", "secret_sauce")
#     assert "Swag Labs" in driver.title


# def test_inventory_page_loaded(driver):
#     login(driver, "standard_user", "secret_sauce")
#     assert driver.find_element("xpath", "//div[@class='inventory_list']") is not None