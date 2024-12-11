from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
import uvicorn
import requests
import json

app = FastAPI()

# Base de datos #

with open("books_db.json", "r", encoding="utf-8") as archivo:
    libros = json.load(archivo) 
    #peliculas es una lista de diccionarios

print(type(libros))
print(libros[0], libros[1])

# Leer archivo

def leer_json(archivo: str) -> dict:
    """Lee el contenido de un archivo JSON y lo devuelve como un objeto de Python."""
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

@app.get('/')
def inicio():
    return "Bienvenid@!!"


@app.get('/buscar_libro')
def buscar(request: Request):
    params = request.query_params
    print(params, "params")
    title = params.get("title")
    resultado = []
    libros = leer_json('books_db.json')
    for libro in libros:
        if title.lower() in libro["title"].lower(): #Utilizo operador in para ver si ese texto esta contenido en el título
            resultado.append(libro)
    
    return JSONResponse(content={"message": f"Se encontraron {len(resultado)} libros.'", 'resultado': resultado})

    
    """
    libros = leer_json('books_db.json')
    for libro in libros:
        if request == libro['title']:
            return libro
    return HTTPException(status_code=404, detail=f"Libro '{titulo}' no encontrado")"""

@app.put('/actualizar_libro')
def actualizar(titulo: str):
    if buscar(titulo):
        libro = buscar(titulo)
    
    return HTTPException(status_code=404, detail=f"Libro '{titulo}' no encontrado")


@app.post('/agregar_libro')
async def agregar(request: Request):
    libro = await request.json()
    libros = leer_json('books_db.json')
    libros.append(libro)

    # Sobrescribir el archivo con los datos actualizados
    try:
        with open("books_db.json", "w", encoding="utf-8") as archivo:
            json.dump(libros, archivo, ensure_ascii=False, indent=4)  # Escribir el archivo con formato bonito, convierte li
    except Exception as e:
        print(str(e))
    return JSONResponse(content={"message": f"Libro '{libro['title']}'agregado correctamente"}) #, "libro": libro