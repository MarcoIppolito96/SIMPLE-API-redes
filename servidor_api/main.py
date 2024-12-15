from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import requests
import json

app = FastAPI()
# Base de datos #

with open("books_db.json", "r", encoding="utf-8") as archivo:
    libros = json.load(archivo) 
    #peliculas es una lista de diccionarios
print(f"Cantidad de libros al iniciar servidor: {len(libros)}")

class Libro(BaseModel):
    title: str
    author: str = None
    country: str = None
    year: int = None
    imageLink: str = None
    language: str = None
    link: str = None
    pages: int = None

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
    params = dict(params)
    clave = list(params.keys())[0]
    #title = params.get("title")
    resultado = []
    libros = leer_json('books_db.json')
    for libro in libros:
        if libro.get(clave) and params[clave].lower() in libro[clave].lower(): #Utilizo operador in para ver si ese texto esta contenido en el título
            resultado.append(libro)
    
    return JSONResponse(content={"message": f"Se encontraron {len(resultado)} libros.'", 'resultado': resultado})


@app.put('/actualizar_libro')
def actualizar_libro(titulo: str, libro_actualizado: Libro):
    libros = leer_json('books_db.json')
    # Buscar el libro por título
    for libro in libros:
        if libro["title"].lower() == titulo.lower():
            # Actualizar los campos proporcionados
            if libro_actualizado.author is not None:
                libro["author"] = libro_actualizado.author
            if libro_actualizado.country is not None:
                libro["country"] = libro_actualizado.country
            if libro_actualizado.year is not None:
                libro["year"] = libro_actualizado.year
            if libro_actualizado.imageLink is not None:
                libro["imageLink"] = libro_actualizado.imageLink
            if libro_actualizado.language is not None:
                libro["language"] = libro_actualizado.language
            if libro_actualizado.link is not None:
                libro["link"] = libro_actualizado.link
            if libro_actualizado.pages is not None:
                libro["pages"] = libro_actualizado.pages
            if libro_actualizado.title is not None:
                libro["title"] = libro_actualizado.title

            with open('books_db.json', 'w', encoding='utf-8') as archivo:
                json.dump(libros, archivo, indent=4, ensure_ascii=False)
            return {"mensaje": "Libro actualizado con éxito", "libro": libro}
    
    # Si no se encuentra el libro
    raise HTTPException(status_code=404, detail=f"Libro '{titulo}' no encontrado")


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
    return JSONResponse(content={"message": f"Libro '{libro['title']}'agregado correctamente"}) 


@app.delete('/eliminar_libro')
def eliminar_libro(titulo: str):
    libros = leer_json('books_db.json')

    libros_filtrados = []
    for libro in libros:
        # Me fijo si es el libro que quiero eliminar, si no lo es entonces lo agrego a la lista que quiero conservar
        if titulo.lower() not in libro['title'].lower():
            libros_filtrados.append(libro)
    
    if len(libros_filtrados) == len(libros):
        return {"mensaje": "No se encontró ningún libro con ese título"}

    # Escribir los libros actualizados de vuelta en el archivo JSON
    with open('books_db.json', 'w', encoding='utf-8') as archivo:
        json.dump(libros_filtrados, archivo, indent=4, ensure_ascii=False)

    return {"mensaje": f"Libro '{titulo}' eliminado correctamente"}