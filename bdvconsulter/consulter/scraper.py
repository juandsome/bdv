from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait

def bdv ():
    # Inicializa el WebDriver para Chrome
    driver = webdriver.Chrome()
    # Navega a una página web
    driver.get("https://bdvenlinea.banvenez.com/")
    # Encuentra un elemento en la página
    username_field = driver.find_element(By.ID, "mat-input-0")

    username_field.send_keys("juanferson")

    username_field.send_keys(Keys.ENTER)

    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "mat-input-1"))
    )
    password_field .send_keys("Papoasado69*")
    password_field .send_keys(Keys.ENTER)

    
    try:
        WebDriverWait(driver, 1).until(
            EC.element_to_be_clickable((By.XPATH, f"//button[text()=' subject ']")),
            
        )
    except:
        print("Los botones no se cargaron en el tiempo esperado.")

    salir=None
    try:
        salir = driver.find_element(By.CSS_SELECTOR, "button[mat-button]")
        print ("boton  salir encontrado")
       
        print(salir.tag_name)   
    except:
        print ("boton de salir no encontrado")

    

    
   
    
   

    logeadourl= driver.page_source

    soup = BeautifulSoup(logeadourl, 'html.parser')
   # print (soup.prettify())


    boton_deseado=None
    
    try:
        botones = driver.find_elements(By.CLASS_NAME, "material-icons")
        print (len(botones))
        for boton in botones:
            print(boton.text)
            if boton.text == "subject":
                boton_deseado = boton
                boton_deseado.click()
                break
    except:
        print ("boton no encontrado")

    
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "mat-cell"))
        )
    finally:
        # Obtener el HTML de la página completamente cargada
        html = driver.page_source

        # Cerrar el navegador
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    elementos_referencia = soup.find_all(class_="mat-column-referencia")
    datos = []
    for elemento in elementos_referencia:
        datos.append(elemento.text.strip())

    

    elemento_a_buscar = "0000930057553"
    coincidencias = list(filter(lambda x: x == elemento_a_buscar, datos))
    if coincidencias:
        print("comprobado")
    else:
        print("no comprobado")

        
       
    if salir:
        driver.execute_script("arguments[0].click();", salir)
        driver.quit()

   

bdv()