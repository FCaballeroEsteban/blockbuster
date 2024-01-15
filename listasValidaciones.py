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


def buscarArchivo(archivo: json, cod):
    for codigo, diccionario in archivo.items():
        print(codigo, diccionario)
        if codigo == cod:
            print(codigo, diccionario['nombre'])

def buscarPeliGen(archivo : json, cod):
    print("ID                  NOMBRE")
    print("--------------------------------------------------------------")
    for codigo, dicc in archivo.items():
        diccioGen = dicc["generos"]
        for codGen, diccioGen in diccioGen.items():
          if(codGen == cod):
            print(codigo, "  ", dicc["nombre"], "  ", dicc["generos"])
        
def buscarPeliculaSipnosisActores(archivo : json, cod):
    print("ID                  NOMBRE")
    print("--------------------------------------------------------------")
    for codigo, dicc in archivo.items():
        diccioGen = dicc["generos"]["sinopsis"]["actores"]
        for codGen, diccioGen in diccioGen.items():
          if(codGen == cod):
            print(codigo, "  ", dicc["nombre"], "  ", dicc["generos"], dicc["actores"])