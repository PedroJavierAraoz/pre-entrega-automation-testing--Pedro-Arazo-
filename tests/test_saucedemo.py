from utils.helpers import login
import pytest


def test_login(driver):

    login(driver,"standard_user", "secret_sauce")
    # Verificamos que la URL cambió a la página de inventario (esto va a fallar)
     