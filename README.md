# 🧪 Proyecto de Automatización - Swag Labs, pre-entrega-automation-testing--Pedro-Araoz-

Este proyecto contiene pruebas automatizadas para la plataforma **Swag Labs** utilizando **Selenium WebDriver** y **Python**.para  cumplir  con la  pre-entrega de  QA automatizacion, Talentoto Tech.

## 🚀 Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:
* **Python 3.x**
* **Google Chrome** (o el navegador de tu preferencia,  pero este  proyecto esta  probadoejecutado usando Google chrome )

## 📦 Instalación

1. Clona este repositorio en tu máquina local.
2. Instala las dependencias necesarias ejecutando el siguiente comando en la terminal de VS Code:

```bash
pip install -r requirements.txt
```

## 🛠️ Cómo Ejecutar las Pruebas

Para correr los tests en tu consola y poder ver la salida de los mensajes `print` o logs; opcion ´-s'; o -sv  para  ver detalles de la  ejecucion,  ejecuta:

```bash
pytest -s 
```
o
```bash
pytest -sv 
```
 o  si deseas  que te genere  el reporte  de la  ejecucion 
 ```bash
 pytest tests/test_saucedemo.py -v --html=reporte.html
 ```
 

## 📂 Estructura del Proyecto

* `tests/` -> Contiene los archivos de pruebas automatizadas.
+ `utils/` -> Contiene las funciones  auxiliares.
* `conftest.py`-> Define  la configuracion  del driver.
* `README.md` -> Documentación del proyecto (este archivo).





Comando para ejecutar las pruebas (por ejemplo: pytest -v --html=reporte.html)
