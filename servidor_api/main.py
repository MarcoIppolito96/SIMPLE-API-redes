from fastapi import FastAPI, HTTPException
import uvicorn
import requests
import json

app = FastAPI()

# Base de datos #

with open("books_db.json", "r", encoding="utf-8") as archivo:
    libros = json.load(archivo) 
    #peliculas es una lista de diccionarios

print(libros[0])

@app.get('/')
def inicio():
    return "Bienvenid@!!"


@app.get('/buscar_libro')
def buscar(titulo: str):
    for libro in libros:
        if titulo == libro['title']:
            return libro
    return HTTPException(status_code=404, detail=f"Libro '{titulo}' no encontrado")

@app.put('/actualizar_libro')
def actualizar(titulo: str):
    if buscar(titulo):
        libro = buscar(titulo)
    

    return HTTPException(status_code=404, detail=f"Libro '{titulo}' no encontrado")
        
