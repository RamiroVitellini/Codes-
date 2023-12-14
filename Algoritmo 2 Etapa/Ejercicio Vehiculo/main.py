from gestor_vehiculo import *
def menu():
    obj_gestor = GestorVehiculo()
    while True:
        menu = """
1.   Crear auto.
2.   Listar autos, indicando tipo de Vehiculo.
3.   Cambiar velocidad de un Vehiculo
4.   Calcular tiempo de viaje de un Vehiculo en una cant de Km pasados por parametro (tiempo = Km / Velocidad)
opcion: """
        opcion = input(menu)
        match opcion:
            case '1':
                obj_gestor.crear_auto()
            case '2':
                obj_gestor.listar_vehiclo()
            case '3':
                obj_gestor.cambiar_velocidad()
            case '4':
                obj_gestor.calcular_tiempo_de_viaje()
            case '5':
                return
            case _:
                print('opcion incorrecta')
if __name__ == "__main__":
    menu()