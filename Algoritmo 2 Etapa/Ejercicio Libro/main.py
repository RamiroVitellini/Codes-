from gestor_libro import *
def menu():
    obj_gestor = GestorBiblioteca()
    while True:
        menu = """
1.   Crear libro.
2.   Cambiar estado libro.
3.   Salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_libro()
            case '2':
                obj_gestor.estado_libro()
            case '3':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()