import json
from menus import menuPrincipal 
from gestorPeliculas import agregarPelicula
from menus import adminPeliculas
from grestorGeneros import adminGeneros
import os
blockbuster = {}
with open("peliculas.json", "r") as f:
    peliculas = json.loads(f.read())
with open("generos.json", "r") as f:
    peliculas = json.loads(f.read())    
bandera = True
while(bandera):
    menuPrincipal()
    opcPrincipal = int(input("Ingresa la opcion que desea hacer:\n"))
    
    
    if opcPrincipal == 5:
        adminPeliculas()
    opcgestorPeli = int(input("Ingrese lo que desea hacer:\n"))    
    if opcgestorPeli == 1:
        agregarPelicula(peliculas)
      
    break
    
          

    

with open("peliculas.json", "w+") as f:
    f.write(json.dumps(peliculas , indent=4))

  
