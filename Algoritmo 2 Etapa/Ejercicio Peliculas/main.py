from gestor_pelicula import *
def menu():
    obj_gestor = GestorPelicula()
    while True:
        menu = """
1. Crear una pelicula y guardar el objeto en una lista de peliculas.
2. Verificar si la pelicula deseada existe en la lista de peliculas.
3. Pedir a la lista de peliculas, todas las de un año.
4. Presentar una pelicula de la lista
5. Cambiar el genero de una pelicula
6. Salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_peliculas()
            case '2':
                obj_gestor.verificar_pelicula_existente()
            case '3':
                obj_gestor.pedir_pelicula_anio()
            case '4':
                obj_gestor.presentar_pelicula()
            case '5':
                obj_gestor.cambiar_genero()
            case '6':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()