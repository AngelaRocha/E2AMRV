import requests
import os
import sys
from bs4 import BeautifulSoup as bs
import webbrowser

#Angela María Rocha Valdez

print("Este script navega en las páginas de noticas de la UANL")
inicioRango = int(input("Pagina inicial para buscar: "))
finRango = int(input("Pagina final para buscar: "))
dependencia = input("Ingrese las siglas de la Facultad a buscar: ")
if inicioRango > finRango:
    inicioRango,finRango = finRango,inicioRango
for i in range (inicioRango,finRango,1):
    url = "https://www.uanl.mx/noticias/page/"+str(i)
    pagina = requests.get (url)
    if pagina.status_code != 200:
        raise TypeError("Pagina no encontrada")
    else:
        soup = bs(pagina.content,"html.parser")
        info = soup.select("h3 a")
        for etiqueta in info:
            url2 = etiqueta.get("href")
            pagina2 = requests.get(url2)
            if pagina2.status_code == 200:
                soup2 = bs(pagina2.content,"html.parser")
                parrafos = soup2.select("p")    
                for elemento in parrafos:
                    if dependencia in elemento.getText():
                        print ("Abriendo",url2)
                        webbrowser.open(url2)
                        break
# En este código podemos observar al principio los distintos import que son
# necesarios para ejecutar este scrip; al principio nos muestra un mensaje
# que nos explica sobre lo que el código se basa(una investigacion de la UANL)
# nos pregunta la pagina por la que queremos comenzar y finalizar, en seguida
# las siglas de la facultad de la que queremos saber las noticias.
# Entrando un poco mas a lo que tiene por detras este codigo, primero, es hacer
# un cambio en caso de que el usuario se haya equivocado al poner el fin e inicio
# de las paginas que quiere investigar, en este caso si el primer numero es mayor
# al segundo que ingreso, inmediatamente invertimos los valores para que sea mas
# lógico. Después con ayuda de un for vamos recorriendo de uno en uno las paginas
# que desea, guardamos en una variable la url de la universidad dejando al final
# la oportunidad de que se dirija a la pagina que se le ha sido otorgada empezar
# e ir pudiendo cambiar de pagina en pagina; en la variable pagina obtenemos los
# resultados de la primera pagina que investigamos, si no nos da permiso directa-
# mente nos da otro status diferente a 200 y esto significa que la pagina no ha
# sido encontrada lo cual terminaria con el proceso de nuestro codigo. En cambio
# si el status nos da 200 quiere decir que tenemos permiso y podemos encontrar
# la facultad y paginas que deseamos; guardamos en variables el contenido de la
# pagina y en la siguiente variable la utilizamos para seleccionarla. Ahora nos
# vamos a otro for que nos ayuda a pasar por cada pagina obteniendo su info.
# y verificando si tenemos acceso, si no es asi salimos de inmediato, pero si
# tenemos acceso con el status 200 a cada pagina, podemos ir directo a obetener
# el contenido y separarlo por parrafos, despues por cada linea de texto y si
# todo sale bien, nos mostratá un mensaje que nos diga que está abriendo la URL
# y por ultimo nos dirige a dicha pagina deseada.

