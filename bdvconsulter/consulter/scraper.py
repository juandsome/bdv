import requests
from bs4 import BeautifulSoup

# Hacer una solicitud a la página
url = "https://www.example.com"
response = requests.get(url)

# Analizar el contenido HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Encontrar todos los enlaces en la página
links = soup.find_all('a')

# Imprimir los enlaces
for link in links:
    print(link.get('href'))