lista_materias = ["matematica", "lengua", "biologia"]
lista_de_alumnos=[[],[],[]]

def pedir_un_str(texto_para_pedir):
    while True:
        variable_str = input(texto_para_pedir)
        if variable_str.isalpha():
            break
        else:
            print('debe ingresar solo letras')
    return variable_str.lower()

def pedir_un_int(texto_para_pedir):
    while True:
        try:
            varaible_int = int(input(texto_para_pedir))
            break
        except Exception as e:
            print('Debe ingresar un valor numerico!')
    return varaible_int

#1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail
def imprimir_lista_alumnos():
    print ("---Nombre---Edad---Mail")
    for i in range(len(lista_de_alumnos[0])):
        print(f'{lista_de_alumnos[0][i]}-{lista_de_alumnos[1][i]}-{lista_de_alumnos[2][i]}')

#2. Permitir al usuario del programa agregar un nuevo alumno (Indicando: nombre_usuario - Edad- Mail
def agregar_alumno():
    while True:
        nombre = pedir_un_str ("Ingrese el nombre del alumno nuevo: ").capitalize()
        if nombre not in lista_de_alumnos:
            lista_de_alumnos[0].append (nombre)
        else:
            print("Nombre de alumno na valido")
        
        edad = pedir_un_int ("Ingrese la edad del alumno nuevo: ")
        if edad not in lista_de_alumnos:
            lista_de_alumnos[1].append (edad)
        else:
            print("Edad de alumno na valido")

        mail = input ("Ingrese el mail del alumno nuevo: ")
        if mail not in lista_de_alumnos:
            lista_de_alumnos[2].append (mail)
        else:
            print("Edad de alumno na valido")
        break

#3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
def editar_edad_alumnos():
    while True:
        nombre_alum = pedir_un_str("Dame el nombre del alumno a cambiar la edad: ").capitalize()
        if nombre_alum in lista_de_alumnos[0]: 
            edad = pedir_un_int ("Ingrese la edad del alumno: ")
            if edad in lista_de_alumnos[1]:
                    nueva_edad = pedir_un_int("Ingrese la nueva edad del alumno:")
                    index = lista_de_alumnos[0].index (nombre_alum)
                    lista_de_alumnos[1][index] = nueva_edad
                    return lista_de_alumnos
            else:
                print ("Valor incorrecto")
        else:
            print('Valor incorrecto')

#4. Ver lista de materias (Formato: Materias) 
def imprimir_lista_materias(lista_materias):
    print ("---MATERIAS---")
    for i in range(len(lista_materias)):
        print(f'{lista_materias[i]}')

#5. Agregar materias al sistema (verificando que no exista previamente)
def agregar_materias():
    nueva_materia = pedir_un_str('Ingrese una materia para agregar : ')
    if nueva_materia not in lista_materias:
        lista_materias.append(nueva_materia)

def menu():
    while True:
        menu = """------> Programa de Gestión de alumnos y Materias <------
    1. Ver lista de alumnos (Formato: nombre_usuario - Edad - Mail)
    2. Agregar un nuevo alumno
    3. Editar la edad de un alumno verificando que este entre 10 y 18 años, se edita mediante el nombre.
    4. Ver lista de materias (Formato: Materias)
    5. Agregar materias al sistema (verificando que no exista previamente)
    6. Salir
Ingrese una opcion: """
        opcion = input(menu)
        if(opcion == "1"):
            imprimir_lista_alumnos()
        elif(opcion == "2"):
            agregar_alumno()
        elif(opcion == "3"):
            editar_edad_alumnos()
        elif(opcion == "4"):
            imprimir_lista_materias(lista_materias)
        elif(opcion == "5"):
            agregar_materias()
        elif(opcion == "6"):
            return
        else:
            print('Opcion incorrecta')

if __name__ == "__main__":
    menu()
