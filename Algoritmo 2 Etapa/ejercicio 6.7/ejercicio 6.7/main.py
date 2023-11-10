from gestor_zoologico import *
def menu():
    obj_gestor = GestorZoologico()
    while True:
        menu = """
1. Crear Empleado.
2. Crear Animal.  
3. Asignar a un empleado un animal a cuidar
4. Cambiar de encargado un animal
5. imprmiir lista de animales 
6. imprimir lista de Empleados
7. Salir
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_empleado()
            case '2':
                obj_gestor.crear_animal()
            case '3':
                obj_gestor.asignar_empelado_a_cuidar()
            case '4':
                obj_gestor.cambiar_encargado_un_animal()
            case '5':
                obj_gestor.imprimir_lista_animales()
            case '6':
                obj_gestor.imprimir_lista_empleados()
            case '7':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()