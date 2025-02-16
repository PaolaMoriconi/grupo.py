from pelicula import CatalogoPelicula, Pelicula
import datetime

catalogo = CatalogoPelicula("Mi Catálogo", "peliculas.txt")


while True:
    print("\n--- Menú ---")
    print("1. Agregar Película")
    print("2. Listar Películas")
    print("3. Eliminar Catálogo")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    try:
        if opcion == '1':
            nombre = input("Ingrese el nombre de la película: ")
            privada = input("¿Es privada? (True/False): ").strip().lower() == 'true'
            hora_ingreso = input("Ingrese la hora de ingreso (YYYY-MM-DD HH:MM:SS): ")

            # Validar el formato de la fecha y hora
            try:
                datetime.datetime.strptime(hora_ingreso, "%Y-%m-%d %H:%M:%S")
            except ValueError:
                print("Formato de fecha y hora incorrecto. Se usará la hora actual.")
                hora_ingreso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            pelicula = Pelicula(nombre, privada, hora_ingreso)
            catalogo.agregar(pelicula)

        elif opcion == '2':
            catalogo.listar()

        elif opcion == '3':
            catalogo.eliminar()

        elif opcion == '4':
            print("¡Hasta luego!")
            break

        else:
            print("Opción inválida.")
    
    except FileNotFoundError as e:
        print(f"Error: No se encontró el archivo: {e}")
    except (IOError, ValueError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {type(e).__name__}: {e}")
