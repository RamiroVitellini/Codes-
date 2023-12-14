from gestor import *
def menu():
    obj_gestor = GestorComputadora()
    while True:
        menu = """
Crear clase GestorComputadora que cuente con las siguientes funciones para un menu
1.   Crear Computadora, indicando tipo y guardar en una lista. Verificando marca y SO de una lista
2.   Listar Computadoras (presentandolos), indicando tipo.
3.   Cambiar SO de una Computadora, verificando una lista de SO disponibles
4.   Listar perifericos
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_computadora()
            case '2':
                obj_gestor.lista_computadora()
            case '3':
                obj_gestor.cambiar_SO()
            case '4':
                obj_gestor.listar_per()
            case '5':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()