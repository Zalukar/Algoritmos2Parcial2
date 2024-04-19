class Nodo:
    def __init__(self, nombre, edad, tipo_empleado, sueldo, sexo):
        self.nombre = nombre
        self.edad = edad
        self.tipo_empleado = tipo_empleado
        self.sueldo = sueldo
        self.sexo = sexo
        self.siguiente = None

# Función para imprimir los datos de un empleado
def imprimir_empleado(empleado):
    print("Nombre:", empleado.nombre)
    print("Edad:", empleado.edad)
    print("Tipo de empleado:", empleado.tipo_empleado)
    print("Sueldo:", empleado.sueldo)
    print("Sexo:", empleado.sexo)
    print()

# Función para imprimir todos los empleados en la lista
def imprimir_todos_empleados(lista):
    nodo_actual = lista
    while nodo_actual:
        imprimir_empleado(nodo_actual)
        nodo_actual = nodo_actual.siguiente

# Función para imprimir el empleado en una posición específica
def imprimir_empleado_en_posicion(lista, posicion):
    contador = 1
    nodo_actual = lista
    while nodo_actual:
        if contador == posicion:
            imprimir_empleado(nodo_actual)
            return
        contador += 1
        nodo_actual = nodo_actual.siguiente
    print("No hay empleado en la posición especificada.")

# Función para contar empleados por tipo
def contar_empleados_por_tipo(lista, tipo):
    contador = 0
    nodo_actual = lista
    while nodo_actual:
        if nodo_actual.tipo_empleado.lower() == tipo.lower():
            contador += 1
        nodo_actual = nodo_actual.siguiente
    return contador


# Función para calcular el salario total de todos los empleados
def calcular_salario_total(lista):
    total = 0
    nodo_actual = lista
    while nodo_actual:
        total += nodo_actual.sueldo
        nodo_actual = nodo_actual.siguiente
    return total

# Función para calcular el promedio de sueldo de todos los empleados
def calcular_promedio_sueldo(lista):
    total = calcular_salario_total(lista)
    cantidad_empleados = 0
    nodo_actual = lista
    while nodo_actual:
        cantidad_empleados += 1
        nodo_actual = nodo_actual.siguiente
    if cantidad_empleados != 0:
        return total / cantidad_empleados
    else:
        return 0

# Función para contar empleados por sexo
def contar_empleados_por_sexo(lista, sexo):
    contador = 0
    nodo_actual = lista
    while nodo_actual:
        if nodo_actual.sexo.lower() == sexo.lower():
            contador += 1
        nodo_actual = nodo_actual.siguiente
    return contador

# Función para imprimir empleados con salario superior a un valor dado
def imprimir_empleados_salario_superior(lista, valor):
    nodo_actual = lista
    while nodo_actual:
        if nodo_actual.sueldo > valor:
            imprimir_empleado(nodo_actual)
        nodo_actual = nodo_actual.siguiente

# Inicializar la cabeza de la lista como None
cabeza_lista = None

# Bucle para permitir al usuario ingresar datos hasta que desee parar
while True:
    nombre = input("Ingrese el nombre del empleado (o 'stop' para detenerse): ")
    if nombre.lower() == 'stop':
        break
    edad = int(input("Ingrese la edad del empleado: "))
    tipo_empleado = input("Ingrese el tipo de empleado (1. Administrativo, 2. Ingeniero, 3. Tecnólogo): ")
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    sexo = input("Ingrese el sexo del empleado (M/F): ")

    nuevo_empleado = Nodo(nombre, edad, tipo_empleado, sueldo, sexo)

    if cabeza_lista is None:
        cabeza_lista = nuevo_empleado
    else:
        nodo_actual = cabeza_lista
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        nodo_actual.siguiente = nuevo_empleado

# Menú de opciones
while True:
    print(" ")
    print("\nMENU:")
    print("1. Imprimir todos los datos de cada empleado.")
    print("2. Mostrar un empleado en particular.")
    print("3. Contar cuántos son Administrativos.")
    print("4. Contar cuántos son Ingenieros.")
    print("5. Contar cuántos son Tecnólogos.")
    print("6. Calcular salario total de todos los empleados.")
    print("7. Calcular promedio del sueldo de todos los empleados.")
    print("8. Contar cuántos son mujeres.")
    print("9. Contar cuántos son hombres.")
    print("10. Imprimir empleados con salario superior a un valor dado.")
    print("11. Salir")
    print(" ")

    opcion = int(input("Ingrese el número de opción: "))
    print(" ")

    if opcion == 1:
        imprimir_todos_empleados(cabeza_lista)
    elif opcion == 2:
        posicion = int(input("Ingrese la posición del empleado: "))
        print(" ")
        imprimir_empleado_en_posicion(cabeza_lista, posicion)
    elif opcion == 3:
        print("Cantidad de empleados Administrativos:", contar_empleados_por_tipo(cabeza_lista, "Administrativo"))
        print(" ")
    elif opcion == 4:
        print("Cantidad de empleados Ingenieros:", contar_empleados_por_tipo(cabeza_lista, "Ingeniero"))
        print(" ")
    elif opcion == 5:
        print("Cantidad de empleados Tecnólogos:", contar_empleados_por_tipo(cabeza_lista, "Tecnólogo"))
        print(" ")
    elif opcion == 6:
        print("Salario total de todos los empleados:", calcular_salario_total(cabeza_lista))
        print(" ")
    elif opcion == 7:
        print("Promedio del sueldo de todos los empleados:", calcular_promedio_sueldo(cabeza_lista))
        print(" ")
    elif opcion == 8:
        print("Cantidad de empleadas mujeres:", contar_empleados_por_sexo(cabeza_lista, "F"))
        print(" ")
    elif opcion == 9:
        print("Cantidad de empleados hombres:", contar_empleados_por_sexo(cabeza_lista, "M"))
        print(" ")
    elif opcion == 10:
        valor = float(input("Ingrese el valor del salario: "))
        print(" ")
        imprimir_empleados_salario_superior(cabeza_lista, valor)
    elif opcion == 11:
        break
    else:
        print("Opción inválida. Por favor, intente nuevamente.")
        print(" ")


##crea una lista que contenga en Python
##Nombre, Edad , Tipo_empleado , Sueldo, Sexo
##Se debe llenar con valores dados por teclado hasta que el usuario no quiera introducir mas datos 
##El tipo empleado es :
##1. Administrativo
##2. Ingeniero
#3 Tecnólogo
#luego de crear menú para imprimir imprimir
#- Imprimir  todos los datos de cada empleado (recorrer la lista )
#- un empleado en particular ( el empleado en la posición X de la lista , x es un número)
# Cuantos son Administrativos
#- Cuantos son Ingenieros 
#- Cuantos son Tecnólogos 
#- Cuantos es salario de todos los empleados 
#- Cuanto es el promedio del sueldo de Todos los Empleados 
#- Cuantos Son mujeres 
#- Cuantos son hombres
#- imprimir el nombre de los empleados y el sueldo de los empleados con salario  superior a un valor dado por teclado.
#Animo 
#La tarea es  entrega grupal (mínimo 4 y máximo 5 estudiantes ) , se entrega un archivo Word, portada, pantallas de ejecución del programa, código fuente  , además el archivo tipo texto con el código , se entregan 2 archivos no pdf  , el codigo se entrega ademas en un archivo txt puro para compilar.
#Da cumplimiento al 100% de los requerimientos solicitados de una forma clara y coherente. La argumentación de cada actividad es completa evidenciando la creatividad del estudiante.