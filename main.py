import json
from menuVisual import * 
from menuFuncion import *

import os
blockbuster = {}
with open("peliculas.json", "r") as f:
    peliculas = json.loads(f.read())

while True: 
    menuPrincipal()
       
    try:
        opcPrincipal = int(input("Ingresa la opcion que desea hacer:\n"))
        if opcPrincipal == 1:
            menuGeneros()
        elif opcPrincipal == 2:
            menuActores()
        elif opcPrincipal == 3:
            menuFormatos()
        elif opcPrincipal == 4:
            menuInformes()              
        elif opcPrincipal == 5:
            menuPeliculas()
        elif opcPrincipal == 6:
            print('Saliendo del Programa....')
            break
        else:
            print('opcion incorrecta')            
    except Exception as error:
        print(error)
        
with open("peliculas.json", "w+") as f:
    f.write(json.dumps(peliculas , indent=4))

  
