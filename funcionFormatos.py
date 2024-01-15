import json
import os
from listasValidaciones import *
from menuFuncion import *
with open("formatos.json", "r") as f:
    formatos = json.loads(f.read())

def crearFormatos():
    bandera = True
    while bandera:
        while True:
            try:
                cod = input("Ingrese el id del formato que desea crear:\n")
                codigo = "F" + str(cod)
                break
            except:
                print('El numero que ha ingresado no es valido')
        validacion = validarExistentes(formatos, codigo)
        if validacion == 1:
            print('El codigo del formato ya existe')
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
                print('Regresando al menu de formatos....') 
                os.system('clear')
                menuGeneros()     
        else:
            print('El codigo no exite en la base de datos puede continuar')

                     
        nombreFormato = str(input("Ingrese el formato:\n"))
        formatos[codigo] = {
            "id": codigo,
            "nombre": nombreFormato
        }
        print('FORMATO CREADO EN LA BASE DE DATOS')
        while True:
            try:
                agregaNuevo = int(input('Desea agregar otro formato?:\n 1. SI\n 2. NO\n'))
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

        with open("formatos.json", "w+") as f:
                    f.write(json.dumps(formatos, indent=4))

def listarFormatos():
    print('----------------Lista de Formatos--------------')
    print('La lista de los formatos son:\n')
    for codigo , diccionario in formatos.items():
        print(codigo,' ', diccionario['nombre'])
        