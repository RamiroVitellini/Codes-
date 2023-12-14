from gestor_evento import *
def menu():
    obj_gestor = GestorEvento()
    while True:
        menu = """
1.   Crear evento.
2.   Listar evento.
3.   Salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_evento()
            case '2':
                obj_gestor.listar_evento()
            case '3':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()