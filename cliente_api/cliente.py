import requests

BASE_URL = "http://127.0.0.1:8000"  # URL base del servidor

"""
       # Validar campos numéricos
    try:
        pages = int(input('Ingresa el número de páginas (ENTER SI NO APLICA): ') or 0)
        year = int(input('Ingresa el año (ENTER SI NO APLICA): ') or 0)
    except ValueError:
        print("Error: Las páginas y el año deben ser números.")
        return

"""

def prueba_inicio():
    """Prueba la ruta de inicio."""
    try:
        response = requests.get(f"{BASE_URL}/")
        print("Respuesta de /:")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con el servidor: {e}")


def buscar_libro():
    """Lógica para buscar un libro."""
    print('1 - Buscar por título')
    print('2 - Buscar por autor')
    print('0 - Salir')
       # Validar campos numéricos
    try:
        opc = int(input('SELECCIONA LA BUSQUEDA ') or 0)
    except ValueError:
        print("Error: La opción debe ser numérica")
        return
    
    if opc == 0:
        return
    elif opc == 1:
        titulo = input('Ingresa el título')
        response = requests.get(BASE_URL+'/buscar_libro', params={'title': titulo})
        data = response.json()
        if 'resultado' in data:
            resultado = data['resultado'] #Acá obtengo los libros quedandome con el parametro resultado (que es donde el servidor me devuelve los libros)
            print(f"Se encontraro.\n {len(resultado)} libros")
            print("Titulos: ")
            for i,libro in enumerate(resultado, start=1):
                print(f"----LIBRO {i}----")
                print(f"{libro['title']}")
            
            resp = int(input('Querés ver informacion de alguno? Ingresa el nro de libro (0 si no queres ver ninguno): '))
            if resp == 0:
                return
            elif 1 <= resp <= len(resultado):
                libro_seleccionado = resultado[resp - 1] # Esto es por que si se selecciona el 1 deberia ser el indice 0 de la lista (al final es un diccionario)
                print("\nInformación detallada del libro:")
                for clave, valor in libro_seleccionado.items():
                    print(f"{clave}: {valor}")
            else:
                print("Número inválido.")
        else:
            print("No se encontraron resultados.")
    elif opc == 2:
        autor = input('Ingresa el autor')
        response = requests.get(BASE_URL+'/buscar_libro', params={'author': autor})
        data = response.json()
        if 'resultado' in data:
            resultado = data['resultado'] #Acá obtengo los libros quedandome con el parametro resultado (que es donde el servidor me devuelve los libros)
            print(f"Se encontraro.\n {len(resultado)} libros")
            print("Titulos: ")
            for i,libro in enumerate(resultado, start=1):
                print(f"----LIBRO {i}----")
                print(f"{libro['title']}")
            
            resp = int(input('Querés ver informacion de alguno? Ingresa el nro de libro (0 si no queres ver ninguno): '))
            if resp == 0:
                return
            elif 1 <= resp <= len(resultado):
                libro_seleccionado = resultado[resp - 1] # Esto es por que si se selecciona el 1 deberia ser el indice 0 de la lista (al final es un diccionario)
                print("\nInformación detallada del libro:")
                for clave, valor in libro_seleccionado.items():
                    print(f"{clave}: {valor}")
            else:
                print("Número inválido.")
        else:
            print("No se encontraron resultados.")


def agregar():
    """Lógica para agregar un libro."""
    title = input('Ingresa el Titulo (ENTER SI NO APLICA)').strip()
    author = input('Ingresa el Autor (ENTER SI NO APLICA)').strip()
    country = input('Ingresa el Pais (ENTER SI NO APLICA)').strip()
    imageLink = input('Ingresa la URL de la imagen (ENTER SI NO APLICA)').strip()
    language = input('Ingresa el lenguaje (ENTER SI NO APLICA)').strip()
    link = input('Ingresa el link (ENTER SI NO APLICA)').strip()

    while True:
        pages = input('Ingresa el numero de páginas (ENTER SI NO APLICA)').strip()
        if pages.strip() == "":
            break
        if pages.isdigit():
            pages = int(pages)
            break
        else:
            print("Por favor ingresá un numero válido")

    while True:
        year = input('Ingresa el año (ENTER SI NO APLICA)').strip()
        if year.strip() == "":
            break
        if year.isdigit():
            year = int(year)
            break
        else:
            print("Por favor ingresá un numero válido")

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
        data = response.json()
        print(f'{data['message']}')
    else:
        print("Error al agregar el libro:", response.text)


def modificar():
    titulo = input("Ingresá el título del libro que queres modificar: ")
    response = requests.get(BASE_URL+'/buscar_libro', params={'title': titulo})
    
    while True:
        if response.status_code != 200:
            titulo = input("Título no encontrado, ingresá el título o parte del mismo que queres modificar: ")
            response = requests.get(BASE_URL+'/buscar_libro', params={'title': titulo})
            continue

        data = response.json()
        resultado = data.get('resultado', []) # Si la clave 'resultado' no esta en el JSON, para que no se produzca un error se asigna una lista vacía
        if len(resultado) == 0:
            print("No se encontraron libros con ese título. Por favor, ingresá un título diferente.")
            titulo = input("Ingresá el título o parte del mismo que querés modificar: ")
            response = requests.get(BASE_URL + '/buscar_libro', params={'title': titulo})
            continue #En caso que se cumpla esto, ignora la parte de que se encuentre resultados (por que no sucede) osea vuelve al input del titulo
        
        # Caso en que se encuentran resultados
        print(f"Se encontró una cantidad de {len(resultado)} libro/s")
        print("Los títulos son: ")
        for i,libro in enumerate(resultado, start=1):
            print(f"----LIBRO {i}----")
            print(f"{libro['title']}")
        resp = int(input('Querés modificar alguno? Ingresa el nro de libro (0 si no queres modificar ninguno de ellos): '))
        if resp == 0:
            return
        elif 1 <= resp <= len(resultado):
            libro_seleccionado = resultado[resp - 1] # Esto es por que si se selecciona el 1 deberia ser el indice 0 de la lista (al final es un diccionario)
            print("\nInformación detallada del libro:")
            for clave, valor in libro_seleccionado.items():
                print(f"{clave}: {valor}")
                while True:
                    try:
                        opc = int(input("Querés modificar este atributo? 1 = Si | 0 = No: ").strip() or 0)
                        if opc not in [0, 1]:
                            print("Error: La opción debe ser 1 o 0.")
                            continue
                    except ValueError:
                        print("Error: La opción debe ser numérica.")
                        continue
                    break
                
                if opc == 1:
                    if isinstance(valor, int):  # Si el valor original es numérico
                        while True:
                            try:
                                nuevo_valor = int(input("Ingresá el nuevo valor (número): ") or None)
                            except ValueError:
                                print("Error: El nuevo valor debe ser un número.")
                                continue
                            break
                    else:  # Para valores no numéricos
                        nuevo_valor = input("Ingresá el nuevo valor: ")
                    
                    libro_seleccionado[clave] = nuevo_valor

        response = requests.put(
                                BASE_URL + '/actualizar_libro',
                                params={'titulo': libro_seleccionado.get('title')},  # Envío el título como parámetro de consulta
                                json=libro_seleccionado
                            )
        if response.status_code == 200:
            print("-- CAMBIOS REALIZADOS CORRECTAMENTE --")
            print("Información actualizada del libro:")
            for clave, valor in libro_seleccionado.items():
                print(f"{clave}: {valor}")
        else:
            print(f"Error al guardar los cambios. Código de estado: {response.status_code}")
            print(f"Mensaje del servidor: {response.text}")
        return

def eliminar():
    titulo = input('Ingresa el título')
    response = requests.get(BASE_URL+'/buscar_libro', params={'title': titulo})
    data = response.json()
    if 'resultado' in data:
        resultado = data['resultado'] #Acá obtengo los libros quedandome con el parametro resultado (que es donde el servidor me devuelve los libros)
        print(f"Se encontraro.\n {len(resultado)} libros")
        print("Titulos: ")
        for i,libro in enumerate(resultado, start=1):
            print(f"----LIBRO {i}----")
            print(f"{libro['title']}")
        
        resp = int(input('Querés eliminar alguno? Ingresa el nro de libro (0 si no queres ver ninguno): '))
        if resp == 0:
            return
        elif 1 <= resp <= len(resultado):
            libro_seleccionado = resultado[resp - 1] # Esto es por que si se selecciona el 1 deberia ser el indice 0 de la lista (al final es un diccionario)
            print("\nLIBRO SELECCIONADO:")
            for clave, valor in libro_seleccionado.items():
                print(f"{clave}: {valor}")
            while True:
                try:
                    opc = int(input("Estas seguro que querés elimiinar este libro? 1 = Si | 0 = No: ").strip() or 0)
                    if opc not in [0, 1]:
                        print("Error: La opción debe ser 1 o 0.")
                        continue
                except ValueError:
                    print("Error: La opción debe ser numérica.")
                    continue
                break
            if opc == 1:
                response = requests.delete(BASE_URL+'/eliminar_libro', params={'titulo': libro_seleccionado.get('title')})
                if response.status_code == 200:
                    data = response.json()
                    print(f'{data['mensaje']}')
                else:
                    print("Error al agregar el libro:", response.text)
            else:
                return
        else:
            print("Número inválido.")
    else:
        print("No se encontraron resultados.")

def main():
    while True:
        print("\n--- MENÚ ---")
        print("0 - Salir")
        print("1 - Agregar")
        print("2 - Modificar")
        print("3 - Eliminar")
        print("4 - Buscar libro")
        
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
            buscar_libro()
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    prueba_inicio()
    main()