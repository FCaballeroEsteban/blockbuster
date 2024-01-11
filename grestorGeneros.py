import json
from menus import gestorGeneros as g

with open("generos.json", "r") as f:
    generos = json.loads(f.read())
def adminGeneros(generos : json):
    id = str(input("Ingrese el id de la pelicula que ingreso:\n"))
    genero = str(input("Ingrese el genero de la pelicula:\n"))
    generos
    generos = {
        "identificacion": id,
        "genero": genero
    }
with open("generos.json", "w+") as f:
    f.write(json.dumps(generos, indent=4))   
    