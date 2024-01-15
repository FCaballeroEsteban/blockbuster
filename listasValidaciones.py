import json
def validarExistentes(archivo : json, cod):
    arrayscodigos = []
    for codigo , diccionario in archivo.items():
        arrayscodigos.append(codigo)
    try:
        arrayscodigos.index(cod)
        return 1
    except:
        return 0
    
def listarItems(archivo: json):
    print("ID                         NOMBRE")
    print("---------------------------------")
    for codigo, diccionario in archivo.items():
        print(codigo , diccionario['nombre'])    