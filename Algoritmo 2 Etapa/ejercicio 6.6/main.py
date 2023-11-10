from gestor_taxis import *
def menu():
    # instancio un objeto de gestor de computadoras para usar sus metodos
    obj_gestor = GestorTaxis()
    while True:
        menu = """
1. Crear instancias de choferes y guardarlos en una lista de choferes
2. Crear instancias de Autos (verificando que haya choferes para ese auto) y guardarlos en una lista de autos
3. Modificar el chofer de un auto
4. Modificar el lugar de residencia del chofer indicando su nombre
5. imprmir lista de choferes (con toda su informacion)
6. imprimir lista de autos (con toda su informacion)
7. Salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_chofer()
            case '2':
                obj_gestor.crear_auto()
            case '3':
                obj_gestor.modificar_chofer()
            case '4':
                obj_gestor.modificar_residencia_v_pro()
            case '5':
                obj_gestor.imprimir_lista_choferes()
            case '6':
                obj_gestor.imprimir_lista_autos()
            case '7':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()