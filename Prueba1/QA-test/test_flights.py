from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


import time


# Iniciar el navegador

page = webdriver.Chrome(executable_path=r"C:\SelePython\chromedriver.exe")

# Abrir la página web a la que deseas iniciar sesión

page.get("https://demo.guru99.com/test/newtours/reservation.php")

# Tipo de Vuelo
radio= page.find_element(By.XPATH, "(//input[@name='tripType'])[2]")
radio.click()
time.sleep(3)

#Numero de Pasajeros
lista_desplegable = Select(page.find_element("name","passCount"))
lista_desplegable.select_by_visible_text("3")

#Pais de residencia 
lista_desplegable = Select(page.find_element("name","fromPort"))
lista_desplegable.select_by_visible_text("London")

#Mes de partida

lista_desplegable = Select(page.find_element("name","fromMonth"))
lista_desplegable.select_by_visible_text("July")

#Dia de de partia

lista_desplegable = Select(page.find_element("name","fromDay"))
lista_desplegable.select_by_visible_text("12")

#Destino
lista_desplegable = Select(page.find_element("name","toPort"))
lista_desplegable.select_by_visible_text("London")


#Mes de regreso

lista_desplegable = Select(page.find_element("name","toMonth"))
lista_desplegable.select_by_visible_text("July")

#Dia de regreso

lista_desplegable = Select(page.find_element("name","toDay"))
lista_desplegable.select_by_visible_text("12")

#Clase en la que viaja
radio= page.find_element(By.XPATH, "(//input[@name='servClass'])[2]")
radio.click()


#Dia de regreso

lista_desplegable = Select(page.find_element("name","airline"))
lista_desplegable.select_by_visible_text("Unified Airlines")

time.sleep(3)

buttom = page.find_element("name","findFlights")

buttom.click()

time.sleep(10)


#........./INCORRECTO

page.get("https://demo.guru99.com/test/newtours/reservation.php")

# Tipo de Vuelo
radio= page.find_element(By.XPATH, "(//input[@name='tripType'])[2]")
radio.click()
time.sleep(3)

#Numero de Pasajeros
lista_desplegable = Select(page.find_element("name","passCount"))
lista_desplegable.select_by_visible_text("3")

#Pais de residencia 
lista_desplegable = Select(page.find_element("name","fromPort"))
lista_desplegable.select_by_visible_text("London")

#Mes de partida

lista_desplegable = Select(page.find_element("name","fromMonth"))
lista_desplegable.select_by_visible_text("February")

#Dia de de partia

lista_desplegable = Select(page.find_element("name","fromDay"))
lista_desplegable.select_by_visible_text("31")

#Destino
lista_desplegable = Select(page.find_element("name","toPort"))
lista_desplegable.select_by_visible_text("London")


#Mes de regreso

lista_desplegable = Select(page.find_element("name","toMonth"))
lista_desplegable.select_by_visible_text("July")

#Dia de regreso

lista_desplegable = Select(page.find_element("name","toDay"))
lista_desplegable.select_by_visible_text("12")

#Clase en la que viaja
radio= page.find_element(By.XPATH, "(//input[@name='servClass'])[2]")
radio.click()


#Dia de regreso

lista_desplegable = Select(page.find_element("name","airline"))
lista_desplegable.select_by_visible_text("Unified Airlines")

time.sleep(3)

buttom = page.find_element("name","findFlights")

buttom.click()

time.sleep(10)
