import json
import os
from listasValidaciones import *
from menuFuncion import *
with open("actores.json", "r") as f:
    actores = json.loads(f.read())

def crearActor():
    bandera = True
    while bandera:
        while True:
            try:
                cod = int(input("Ingrese el id del Actor que desea crear:\n"))
                codigo = "A" + str(cod)
                 
                break
            except:
                print('El numero que ha ingresado no es valido')
        validacion = validarExistentes(actores, codigo)
        if validacion == 1:
            print('El codigo del actor ya existe')
            bandera2 = True
            while bandera2:
                try:
                    editaropc = int(input('Desea editarlo?:\n 1. SI\n 2. NO\n'))
                    if(editaropc !=1 and editaropc !=2):
                        editaropc = 1/0
                    bandera2 = False
                except:
                    print('El numero ingresado no es valido')
            if(editaropc == 1):
                print('Puede seguir editando....')        
            elif editaropc == 2:
                print('Regresando al menu de actores....') 
                os.system('clear')
                menuActores()     
        else:
            print('El codigo no exite en la base de datos puede continuar')

                     
        nombreActor = str(input("Ingrese el nombre:\n"))
        actores[codigo] = {
            "id": codigo,
            "nombre": nombreActor
        }
        print('ACTOR CREADO EN LA BASE DE DATOS')
        while True:
            try:
                agregaNuevo = int(input('Desea agregar otro Actor?:\n 1. SI\n 2. NO\n'))
                if agregaNuevo == 1:
                    os.system('clear')    
                    break
                elif agregaNuevo == 2:
                    bandera = False
                    break
                else:
                    print('El numero que ha ingresado no es valido')
            except:
                print('El numero que ha ingresado no es valido')

        with open("actores.json", "w+") as f:
                    f.write(json.dumps(actores, indent=4))

def listarActores():
    print('----------------Lista de Actores--------------')
    print('La lista de los actores son:\n')
    for codigo , diccionario in actores.items():
        print(codigo,' ', diccionario['nombre'])