import json
import os
from listasValidaciones import *
from menuFuncion import *
with open("formatos.json", "r") as f:
    formatos = json.loads(f.read())
with open("generos.json", "r") as f:
    generos = json.loads(f.read())
with open("peliculas.json", "r") as f:
    peliculas = json.loads(f.read())

def crearPelicula():
    bandera = True
    while bandera:
        while True:
            try:
                cod = int(input("Ingrese el id de la pelicula que desea crear:\n"))
                codigo = "P" + str(cod)
                break
            except:
                print('El numero que ha ingresado no es valido')
        validacion = validarExistentes(peliculas, codigo)
        if validacion == 1:
            print('El codigo de la pelicula ya existe')
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
                print('Regresando al menu de las peliculas....') 
                os.system('clear')
                menuGeneros()     
        else:
            print('El codigo no exite en la base de datos puede continuar')
        nombreGenero = str(input("Ingrese el nombre de la pelicula:\n"))    
        bandera3 = True
        while bandera3:             
            try:
                duracion = float(input('Ingrese la duracion de la pelicula en horas:\n'))
                bandera3 = False
            except:
                print('El numero ingresado no es valido') 
        sinopsis = str(input('Ingrese la sinopsis de la pelicula:\n'))

        generoAsignar = asignarGenero(generos, peliculas, codigo)  
        formatoAsignar = asignarFormatos(formatos, peliculas, codigo)          
        peliculas[codigo] = {
            "id": codigo,
            "nombre": nombreGenero,
            "duracion" : str(duracion) + " " + "Horas",
            "sinopsis" : sinopsis,
            "generos": generoAsignar,
            "formatos": formatoAsignar
        }
        print('PELICULA CREADA EN LA BASE DE DATOS')
        while True:
            try:
                agregaNuevo = int(input('Desea agregar otra pelicula?:\n 1. SI\n 2. NO\n'))
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

        with open("peliculas.json", "w+") as f:
                    f.write(json.dumps(peliculas, indent=4))

def listarPelicula():
    print('----------------Lista de Generos--------------')
    print('La lista de las peliculas son:\n')
    for codigo , diccionario in peliculas.items():
        print(codigo, ' ', diccionario['nombre'])

def asignarGenero(generos: json, peliculas: json, codigo) -> dict:
    generoAsignar = {}
    banderaOtro = True
    while banderaOtro:
        print("A continuacion se mostraran todos los generos existentes en la base de datos:\n")
        listarItems(generos)
        bandera = True
        while bandera:
            try:
                opc = int(input('Elija una opcion:\n 1. Asignar un genero a la lista\n2. crear un nuevo genero y asignarlo\n3. Salir\n'))
                if opc !=1 and opc !=2:
                    opc = 1/0
                bandera = False
            except:
                print('El numero que ha ingresado no es valido')  
        if  opc == 1:
            bandera1 = True
            while bandera1:   
                    opcGen = str(input('Ingrese el id del genero a asignar:\n'))
                    validacion = validarExistentes(generos, opcGen)
                    if validacion ==1:
                        generoAsignar[opcGen] = generos[opcGen]
                        
                        bandera1 = False
                    elif validacion == 0:
                        print('EL genero ingresado no se encuetra en la base de datos')

        elif opc == 2:
            crearGenero()
            print('EL genero ha sido creado :D\n')
            bandera2 = True
            while bandera2:
                try:
                    opcAsig = int(input('¿Desea asignar el nuevo genero creado?\n1 SI\n 2. NO\n'))
                    if opcAsig !=1 and opcAsig !=2:
                        opcAsig = 1/0
                    bandera2 = False
                except:
                    print('EL numero ingresado no es valido')    
            if opcAsig == 1:
                asignarGenero(generos, peliculas, codigo)
            elif opcAsig == 2:
                menuPeliculas()
        elif opc == 3:
            menuPeliculas()
        while True:
            try:
                agregaNuevo = int(input('Desea agregar otro genero?:\n 1. SI\n 2. NO\n'))
                if agregaNuevo == 1:
                    os.system('clear')    
                    break
                elif agregaNuevo == 2:
                    banderaOtro = False
                    break
                else:
                    print('El numero que ha ingresado no es valido')
            except:
                print('El numero que ha ingresado no es valido')
    return generoAsignar  



def asignarFormatos(formatos: json, peliculas: json, codigo) -> dict:
    formatoAsignar = {}
    banderaOtro = True
    while banderaOtro:
        print("A continuacion se mostraran todos los formatos existentes en la base de datos:\n")
        listarItems(formatos)
        bandera = True
        while bandera:
            try:
                opc = int(input('Elija una opcion:\n 1. Asignar un formato a la lista\n2. crear un nuevo formato y asignarlo\n3. Salir\n'))
                if opc !=1 and opc !=2:
                    opc = 1/0
                bandera = False
            except:
                print('El numero que ha ingresado no es valido')  
        if  opc == 1:
            bandera1 = True
            while bandera1:   
                    opcGen = str(input('Ingrese el id del formato a asignar:\n'))
                    validacion = validarExistentes(formatos, opcGen)
                    if validacion ==1:
                        formatoAsignar[opcGen] = formatos[opcGen]
                        
                        bandera1 = False
                    elif validacion == 0:
                        print('EL formato ingresado no se encuetra en la base de datos')

        elif opc == 2:
            crearGenero()
            print('EL formato ha sido creado :D\n')
            bandera2 = True
            while bandera2:
                try:
                    opcAsig = int(input('¿Desea asignar el nuevo formato creado?\n1 SI\n 2. NO\n'))
                    if opcAsig !=1 and opcAsig !=2:
                        opcAsig = 1/0
                    bandera2 = False
                except:
                    print('EL numero ingresado no es valido')    
            if opcAsig == 1:
                asignarFormatos(formatos, peliculas, codigo)
            elif opcAsig == 2:
                menuPeliculas()
        elif opc == 3:
            menuPeliculas()
        while True:
            try:
                agregaNuevo = int(input('Desea agregar otro formato?:\n 1. SI\n 2. NO\n'))
                if agregaNuevo == 1:
                    os.system('clear')    
                    break
                elif agregaNuevo == 2:
                    banderaOtro = False
                    break
                else:
                    print('El numero que ha ingresado no es valido')
            except:
                print('El numero que ha ingresado no es valido')
    return formatoAsignar                   
                    
def asignarActor(actores: json, peliculas: json, codigo) -> dict:
    actorAsignar = {}
    banderaOtro = True
    while banderaOtro:
        print("A continuacion se mostraran todos los generos existentes en la base de datos:\n")
        listarItems(generos)
        bandera = True
        while bandera:
            try:
                opc = int(input('Elija una opcion:\n 1. Asignar un genero a la lista\n2. crear un nuevo genero y asignarlo\n3. Salir\n'))
                if opc !=1 and opc !=2:
                    opc = 1/0
                bandera = False
            except:
                print('El numero que ha ingresado no es valido')  
        if  opc == 1:
            bandera1 = True
            while bandera1:   
                    opcGen = str(input('Ingrese el id del genero a asignar:\n'))
                    validacion = validarExistentes(generos, opcGen)
                    if validacion ==1:
                        generoAsignar[opcGen] = generos[opcGen]
                        
                        bandera1 = False
                    elif validacion == 0:
                        print('EL genero ingresado no se encuetra en la base de datos')

        elif opc == 2:
            crearGenero()
            print('EL genero ha sido creado :D\n')
            bandera2 = True
            while bandera2:
                try:
                    opcAsig = int(input('¿Desea asignar el nuevo genero creado?\n1 SI\n 2. NO\n'))
                    if opcAsig !=1 and opcAsig !=2:
                        opcAsig = 1/0
                    bandera2 = False
                except:
                    print('EL numero ingresado no es valido')    
            if opcAsig == 1:
                asignarGenero(generos, peliculas, codigo)
            elif opcAsig == 2:
                menuPeliculas()
        elif opc == 3:
            menuPeliculas()
        while True:
            try:
                agregaNuevo = int(input('Desea agregar otro genero?:\n 1. SI\n 2. NO\n'))
                if agregaNuevo == 1:
                    os.system('clear')    
                    break
                elif agregaNuevo == 2:
                    banderaOtro = False
                    break
                else:
                    print('El numero que ha ingresado no es valido')
            except:
                print('El numero que ha ingresado no es valido')
    return generoAsignar                                
            

