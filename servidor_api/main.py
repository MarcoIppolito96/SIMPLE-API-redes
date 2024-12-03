from fastapi import FastAPI, HTTPException
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

def abrir_bd(opc):
    with open("books_db.json", opc, encoding="utf-8") as archivo:
        libros = json.load(archivo) 

# Leer archivo

def leer_json(archivo):
    """Lee el contenido de un archivo JSON y lo devuelve como un objeto de Python."""
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

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


@app.post('/agregar_libro')
def agregar(libro: dict):
    libros = leer_json('books_db.json')

    libros.append(libro)

    # Sobrescribir el archivo con los datos actualizados
    try:
        with open("books_db.json", "w", encoding="utf-8") as archivo:
            json.dump(libros, archivo, ensure_ascii=False, indent=4)  # Escribir el archivo con formato bonito
    except Exception as e:
        print(str(e))