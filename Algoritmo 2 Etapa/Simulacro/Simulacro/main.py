from gestor_biblioteca import *
def menu():
    obj_gestor = GestorBiblioteca()
    while True:

        menu = """------> Programa de Gestión de Biblioteca <------
    1.   Crear instancias de libros y guardalos en una lista de libros. 
    2.   Listar libros disponibles.
    3.   Cambiar el estado (Alquilar o devolver) de un libro
    4.   Salir
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == "1"):
            obj_gestor.crear_libros
        elif(opcion == "2"):
            obj_gestor.listar_libros
        elif(opcion == "3"):
            pass
        else:
            print('Opcion incorrecta')

if __name__ == "__main__":
    menu()
