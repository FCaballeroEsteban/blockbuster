import json
from menuVisual import *
from funcionGeneros import crearGenero
from funcionGeneros import listarGeneros
from funcionActores import crearActor
from funcionActores import listarActores
from funcionFormatos import crearFormatos
from funcionFormatos import listarFormatos
from funcionPeliculas import crearPelicula
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
                "eliminarPelicula()"
            elif opcPelicula == 4:
                "eliminarActor"
            elif opcPelicula == 5:
                "buscarPelicula()"
            elif opcPelicula == 6:
                "listarPelicula"
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
                "listarPeliculaGenero()"
            elif opcInforme == 2:
                "listarPeliculaSilvestre()"
            elif opcInforme == 3:
                "buscarPeliculaSipnosisActores()"
            elif opcInforme == 4:
                os.system('clear')
                menuPrincipal()
                break
            else:
                print('Opcion Incorrecta')
        except:
            print('ERROR')                    
      


        
