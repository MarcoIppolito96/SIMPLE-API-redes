import requests

BASE_URL = "http://127.0.0.1:8000"  # URL base del servidor


def prueba_inicio():
    """Prueba la ruta de inicio."""
    try:
        response = requests.get(f"{BASE_URL}/")
        print("Respuesta de /:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el servidor: {e}")


def agregar():
    """Lógica para agregar un libro."""
    title = input('Ingresa el Titulo (ENTER SI NO APLICA)')
    author = input('Ingresa el Autor (ENTER SI NO APLICA)')
    country = input('Ingresa el Pais (ENTER SI NO APLICA)')
    imageLink = input('Ingresa la URL de la imagen (ENTER SI NO APLICA)')
    language = input('Ingresa el lenguaje (ENTER SI NO APLICA)')
    link = input('Ingresa el link (ENTER SI NO APLICA)')
    pages = int(input('Ingresa el numero de páginas (ENTER SI NO APLICA)'))
    year = int(input('Ingresa el año (ENTER SI NO APLICA)'))

    nuevolibro = {
    "author": author,
    "country": country,
    "imageLink": imageLink,
    "language": language,
    "link": link,
    "pages": pages,
    "title": title,
    "year": year}

    response = requests.post(BASE_URL+'/agregar_libro', json = nuevolibro)
    if response.status_code == 200:
        print("Libro agregado correctamente:", response.json())
    else:
        print("Error al agregar el libro:", response.text)


def modificar():
    """Lógica para modificar un libro."""
    print("Funcionalidad para modificar un libro (no implementada aún).")


def eliminar():
    """Lógica para eliminar un libro."""
    print("Funcionalidad para eliminar un libro (no implementada aún).")


def main():
    while True:
        print("\n--- MENÚ ---")
        print("0 - Salir")
        print("1 - Agregar")
        print("2 - Modificar")
        print("3 - Eliminar")
        print("4 - Probar conexión")
        
        try:
            opc = int(input("Selecciona una opción: "))
        except ValueError:
            print("Por favor, ingresa un número válido.")
            continue
        
        if opc == 0:
            print("¡Gracias por usar el programa! Hasta luego.")
            break
        elif opc == 1:
            agregar()
        elif opc == 2:
            modificar()
        elif opc == 3:
            eliminar()
        elif opc == 4:
            prueba_inicio()
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    prueba_inicio()
    main()