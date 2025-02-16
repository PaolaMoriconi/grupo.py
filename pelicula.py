import os
import datetime

class Pelicula:
    def __init__(self, nombre, privada, hora_ingreso=None):
        self.nombre = nombre
        self.__privada = privada  # Atributo privado
        self.hora_ingreso = hora_ingreso or datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def get_privada(self):
        return self.__privada

    def set_privada(self, privada):
        self.__privada = privada

    def __str__(self):
        ahora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Hora actual al mostrar la película
        return f"Título: {self.nombre}, Privada: {self.__privada}, Ingreso: {self.hora_ingreso}, Hora Actual: {ahora}"

class CatalogoPelicula:
    def __init__(self, nombre, ruta_archivo):
        self.nombre = nombre
        self.ruta_archivo = ruta_archivo
        self.peliculas = []  # Inicializa la lista vacía
        self.cargar_peliculas()  # Carga las películas existentes



    def agregar(self, pelicula):
        self.peliculas.append(pelicula)
        self.guardar_peliculas()
        print(f"Película '{pelicula.nombre}' agregada al catálogo {pelicula.hora_ingreso}.")

    def listar(self):
        if not self.peliculas:
            print("El catálogo está vacío.")
        else:
            for pelicula in self.peliculas:
                print(pelicula)

    def eliminar(self):
        if os.path.exists(self.ruta_archivo):
            os.remove(self.ruta_archivo)
            self.peliculas = []
            print("El catálogo ha sido eliminado.")
        else:
            print("El catálogo no existe.")

    def cargar_peliculas(self):
        try:
            with open(self.ruta_archivo, 'r') as archivo:
                self.peliculas = [
                    Pelicula(nombre, privada == 'True', hora_ingreso)
                    for nombre, privada, hora_ingreso in (
                        linea.strip().split(',') for linea in archivo
                    )
                ]
        except FileNotFoundError:
            print("El archivo no existe, se creará uno nuevo al guardar.")
            self.peliculas = []
        except Exception as e:
            print(f"Error al cargar películas: {e}")
            self.peliculas = []



    def guardar_peliculas(self):
        try:
            with open(self.ruta_archivo, 'w') as archivo:
                for pelicula in self.peliculas:
                    archivo.write(f"{pelicula.nombre},{pelicula.get_privada()},{pelicula.hora_ingreso}\n")
        except Exception as e:
            print(f"❌💥⚠️Error al guardar películas: {e}")
