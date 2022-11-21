from bs4 import BeautifulSoup
from csv import writer
import requests

url = "https://www.tucasa.com/compra-venta/viviendas/madrid/?r=&idz=0028&ord=&pgn="

#Contador para el número de páginas donde extraer datos
numPagina = 1

#Escribir fichero csv, con una cabecera

with open('../dataset/housing.csv', 'w', encoding='utf8', newline='') as f:
    thewriter = writer(f)
    header = ['Área Geográfica', 'Metros', 'Precio-Metro', 'Ultima Actualizacion']
    thewriter.writerow(header)

    #Extraeremos información de las 10 primeras páginas de la web
    while numPagina <= 10:

        print(numPagina)

        #Requests para acceder a la web
        page = requests.get("https://www.tucasa.com/compra-venta/viviendas/madrid/?r=&idz=0028&ord=&pgn="+str(numPagina))
        statusCode = page.status_code

        #Extraemos la información del "div" contenedor
        soup = BeautifulSoup(page.content, 'html.parser')
        lists = soup.find_all('div', class_="contenedor-descripcion-inmueble")

        #Se itera en la lista, y con el método ".find" se busca la etiqueta y el nombre
        #De la clase, luego quitamos la etiquita con ".text"
        for list in lists:
            title = list.find('span', class_="titulo-inmueble").text
            metros = list.find('li', class_="metros-cuadrados").text
            preciometro = list.find('li', class_="precio-metro").text
            actualizacion = list.find('span', class_="fecha-actualizacion").text

            info = [title, metros, preciometro, actualizacion]
            thewriter.writerow(info)

        #Sumamos el contador para pasar a la página siguiente
        numPagina += 1
