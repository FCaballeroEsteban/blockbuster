import json
from menuVisual import *
from funcionGeneros import crearGenero
from funcionGeneros import listarGeneros
from funcionActores import crearActor
from funcionActores import listarActores
from funcionFormatos import crearFormatos
from funcionFormatos import listarFormatos
from funcionPeliculas import crearPelicula
from listasValidaciones import buscarArchivo
from funcionPeliculas import listarPelicula
from listasValidaciones import buscarPeliGen
from listasValidaciones import buscarPeliculaSipnosisActores
with open("actores.json", "r") as f:
    actores = json.loads(f.read())

with open("peliculas.json", "r") as f:
    peliculas = json.loads(f.read())
import os

def menuGeneros():
    while True:
        menuVisualGeneros()
        
        try:
            opcGenero = int(input('Ingrese la opcion que desea:\n'))
            if opcGenero == 1:
                crearGenero()
            elif opcGenero == 2:
                listarGeneros()
            elif opcGenero == 3:
                os.system('clear')
                menuPrincipal()
                break
            else:
                print('Opcion Incorrecta')
        except:
            print('Error') 

def menuActores():
   while True:
       menuVisualActores()
       try:
           opcActor = int(input('Ingrese la opcion que desea:\n'))
           if opcActor == 1:
               crearActor()
           elif opcActor == 2:
               listarActores()
           elif opcActor == 3:
               os.system('clear')
               menuPrincipal()
               break
           else:
               print('opcion Incorrecta')
       except:
           print('Error')
                            
def menuFormatos():
    while True:
        menuVisualFormatos()
        try:
            opcFormato = int(input('Ingrese la opcion a realizar:\n'))
            if opcFormato == 1:
                crearFormatos()
            elif opcFormato == 2:
                listarFormatos()
            elif opcFormato == 3:
                os.system('clear')
                menuPrincipal() 
                break
            else:
                print('opcion Incorrecta')
        except:
            print('Error') 

def menuPeliculas():  
    while True:          
        menuVisualPeliculas()
        try:
            opcPelicula = int(input('Ingrese la opcion a realizar:\n'))
            if opcPelicula == 1:
                crearPelicula()
            elif opcPelicula == 2:
                "editarPelicula()"
            elif opcPelicula == 3:
                opc = input('Ingrese el id de la pelicula que desea eliminar:\n')
                del peliculas[opc]
                print('La pelicula ha sido eliminada')
                with open("peliculas.json", "w+") as f:
                    f.write(json.dumps(peliculas, indent=4))

            elif opcPelicula == 4:
                opc = input('Ingrese el id del Actor que desea eliminar:\n')
                del actores[opc]
                print('El actor ha sido eliminado')
                with open("actores.json", "w+") as f:
                    f.write(json.dumps(actores, indent=4))
            elif opcPelicula == 5:
                opc = input('Ingrese el id de la pelicula que desea buscar')
                buscarArchivo(peliculas , opc)
            elif opcPelicula == 6:
                listarPelicula()
            elif opcPelicula == 7:
                os.system('clear')
                menuPrincipal()
                break
            else: 
                print('Opcion Incorrecta')
        except:
            print('ERROR')                                  

def menuInformes():
    while True:
        menuVisualInformes()
        try:
            opcInforme = int(input('Ingrese la opcion a realizar:\n'))
            if opcInforme == 1:
                opc = input('Ingrese el id del genero que desea buscar:\n')
                buscarPeliGen(peliculas, opc)
            elif opcInforme == 2:
                "listarPeliculaSilvestre()"
            elif opcInforme == 3:
                opc = input('Ingrese el id de la pelicula y mostrar sinopsis y actores que desea buscar:\n')
                buscarPeliculaSipnosisActores(peliculas,opc)
            elif opcInforme == 4:
                os.system('clear')
                menuPrincipal()
                break
            else:
                print('Opcion Incorrecta')
        except:
            print('ERROR')                    
      


        
