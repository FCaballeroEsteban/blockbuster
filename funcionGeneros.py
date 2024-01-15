import json
import os
from listasValidaciones import *
from menuFuncion import *
with open("generos.json", "r") as f:
    generos = json.loads(f.read())

def crearGenero():
    bandera = True
    while bandera:
        while True:
            try:
                cod = input("Ingrese el id del genero que desea crear:\n")
                codigo = "G" + str(cod)
                break
            except:
                print('El numero que ha ingresado no es valido')
        validacion = validarExistentes(generos, codigo)
        if validacion == 1:
            print('El codigo del genero ya existe')
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
                print('Regresando al menu de generos....') 
                os.system('clear')
                menuGeneros()     
        else:
            print('El codigo no exite en la base de datos puede continuar')

                     
        nombreGenero = str(input("Ingrese el genero:\n"))
        generos[codigo] = {
            "id": codigo,
            "nombre": nombreGenero
        }
        print('GENERO CREADO EN LA BASE DE DATOS')
        while True:
            try:
                agregaNuevo = int(input('Desea agregar otro genero?:\n 1. SI\n 2. NO\n'))
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

        with open("generos.json", "w+") as f:
                    f.write(json.dumps(generos, indent=4))

def listarGeneros():
    print('----------------Lista de Generos--------------')
    print('La lista de los generos son:\n')
    for codigo , diccionario in generos.items():
        print(codigo,' ', diccionario['nombre'])
       







   
