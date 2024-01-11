import json
peliculas = {}
patch = "peliculas.json"
with open(patch, "r") as f:
    peliculas = json.loads(f.read())

def agregarPelicula(peliculas : json):
    id = str(input("Ingrese el id de la pelicula que desea agregar:\n"))
    nombre = str(input("Ingrese el nombre de la pelicula:\n"))
    duracion = str(input("Ingrese la duracion de la pelicula:\n"))
    sinopsis = str(input("Ingrese la sinopsis de la pelicula:\n"))

    for llave , valor in peliculas:
        peliculas[llave][valor].append[id]
        


    peliculas = {
        "identificacion" : id,
        "nombre" : nombre,
        "duracion" : duracion,
        "sinopsis" : sinopsis,
        "generos" : {}
    }   
    return "Pelicula agregada"
with open(patch, "w+") as f:
    f.write(json.dumps(peliculas, indent=4))    


