
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from playwright.sync_api import Page
import pytest
import time


# Iniciar el navegador

page = webdriver.Chrome(executable_path=r"C:\SelePython\chromedriver.exe")

# Abrir la página web a la que deseas iniciar sesión



# Incorrecto

page.get("https://demo.guru99.com/test/newtours/index.php")

page.implicitly_wait(5)

username = page.find_element("name","userName")

username.send_keys("A$5ñ*3")

password = page.find_element("name","password")

password.send_keys("A$5ñ*3")

username.send_keys(Keys.ENTER)

page.implicitly_wait(10)

#Ingreso de Administrador al sistemas Usuario Incorrecto Password correcto

username = page.find_element("name","userName")

username.send_keys("A$5ñ*3")

password = page.find_element("name","password")

password.send_keys("admin")

username.send_keys(Keys.ENTER)

page.implicitly_wait(10)

#Ingreso de Administrador al sistemas Usuario Correcto Password Incorrecto

username = page.find_element("name","userName")

username.send_keys("A$5ñ*3")

password = page.find_element("name","password")

password.send_keys("admin")

username.send_keys(Keys.ENTER)

page.implicitly_wait(10)
# Encontrar los campos de entrada de usuario y contraseña

username = page.find_element("name","userName")

username.send_keys("admin")

password = page.find_element("name","password")

password.send_keys("admin")

username.send_keys(Keys.ENTER)
 
time.sleep(3)

#Ingreso de Administrador al sistemas sin colocar ninguna credencial
page.get("https://demo.guru99.com/test/newtours/index.php")

page.implicitly_wait(5)

username = page.find_element("name","userName")

username.send_keys("")

password = page.find_element("name","password")

password.send_keys("")

username.send_keys(Keys.ENTER)

page.implicitly_wait(10)