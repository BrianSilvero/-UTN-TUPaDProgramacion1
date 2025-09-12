#1) Crear una lista con las notas de 10 estudiantes. 
# • Mostrar la lista completa.
# • Calcular y mostrar el promedio.
# • Indicar la nota más alta y la más baja

"""notas = [5,9,10,9.5,8,7,4.5,6,5.5,6]
print(f"-Las notas son: {notas}")

sumatoria = 0
cant_alumno = 10

#Sumamos los promedios a traves de un for: 
for i in range(len(notas)):
    sumatoria += notas[i]

#Mostramos el resultado del promedio
print(f"El promedio de las notas es de: {sumatoria/cant_alumno}")

# Recorremos la lista con un For para adquirir la nota mas alta y mas baja
nota_mas_baja = notas[0]
nota_mas_alta = notas[0]


for i in range(len(notas)):
    if notas[i] > nota_mas_alta:
        nota_mas_alta = notas[i]
        
    if notas[i] < nota_mas_baja:
       nota_mas_baja = notas[i]

# La otra forma mas rapida es con la funcion min() y max()
nota_maxima = max(notas)
nota_min = min(notas)

# Mostramos las notas mas altas y mas baja
print(f"La nota mas alta es {nota_mas_alta} y la nota mas baja es {nota_mas_baja}")
print(f"La nota mas alta es {nota_maxima} y la nota mas baja es {nota_min}")"""

# 2) Pedir al usuario que cargue 5 productos en una lista. 
# • Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# • Preguntar al usuario qué producto desea eliminar y actualizar la lista.

"""lista_productos = []
print("---ESCRIBA 5 PRODUCTOS PARA AGREGAR A LA LISTA---")
for i in range(5):
    producto = str(input(f"Escriba un producto ({i+1}/5): ").capitalize())
    lista_productos.append(producto)

#Mostramos las listas con el metodo sorted()
lista_ordenada = sorted(lista_productos)
print(lista_ordenada)


#Preguntamos que producto desea eliminar y corroboramos que el producto este en la lsita
while True:
    producto_a_eliminar = str(input(f"Escriba el producto a eliminar: ").capitalize())
    if producto_a_eliminar in lista_productos:
        lista_productos.remove(producto_a_eliminar)
        break
    else:
        print(f"El producto '{producto_a_eliminar}' no se encuentra en la lista intententelo nuevamente.")

#Mostramos la lista actualizada
print(f"Producto '{producto_a_eliminar}' eliminado de la lista con exitos!")
print("---Lista actualizada---")

print(lista_productos)"""

# 3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# • Crear una lista con los pares y otra con los impares.
# • Mostrar cuántos números tiene cada lista.

"""lista = [1,2,90,87,43,32,21,11,55,66,33,27,17,13,14]
pares = []
impares = []

for num in  lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

# Mostrar lista de pares e impares:
print(f"Lista de pares: {pares}")
print(f"Lista de impares: {impares}")
print(f"La cantidad de numeros pares es de: {len(pares)}")
print(f"La cantidad de numeros impares es de: {len(impares)}")"""

# 4) Dada una lista con valores repetidos: 
# • Crear una nueva lista sin elementos repetidos.
# • Mostrar el resultado

"""datos = [1,3,5,3,7,1,9,5,3]

lista_nueva = []

for num in datos:
    if len(lista_nueva) != 0:
        if num in lista_nueva:
            continue
        else:
            lista_nueva.append(num)
    else:
        lista_nueva.append(num)

print("---La lista nueva quedaria----")
print(lista_nueva)"""

#Tambien se puede realizar de la siguiente forma sin tanta logica:

"""for num in datos:
    if num not in lista_nueva:
        lista_nueva.append(num)


print(lista_nueva)"""

# 5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# • Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# • Mostrar la lista final actualizada.

"""lista_alumnos = ["Brian", "David", "Melina","Angela", "Priscila", "Jeanette", "Gabriel", "Juan"]

#Recorremos la lista para que pueda seleccionar el alumno
for alumno in lista_alumnos:
        print(f"-{alumno}")

#Creamos un ciclo while para preguntar si desea agregar otro alumno
while True:
    opcion = input("\nDesea agregar otro alumno?(SI/NO):").upper()
    if opcion == "SI":
        agregar = str(input(f"\nIndique el nombre del alumno:").strip().capitalize())
        lista_alumnos.append(agregar)
    elif opcion == "NO":
        break
    else:
        print("Opción no valida. Intentelo nuevamente.")

#Creamos un ciclo while para preguntar si desea eliminar algun  alumno

while True:
    opcion = input("\nDesea eliminar algun alumno?(SI/NO):").upper()
    if opcion == "SI":
        eliminar = str(input(f"\nIndique el nombre del alumno a eliminar:").capitalize())
        if eliminar in lista_alumnos:
            lista_alumnos.remove(eliminar)
            print("Lista actualizada:", lista_alumnos)
        else:
            print(f"{eliminar} no se encuentra en la lista.")
    elif opcion == "NO":
        break
    else:
        print("Opción no valida. Intentelo nuevamente.")

print("---Lista Actualizada---")
print(lista_alumnos)"""

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha (el último pasa a ser el primero).

"""numeros = [1,2,3,4,5,6,7]

# Usamo un concatenacion 
numeros = [numeros[-1]] + numeros[:-1]
print(numeros)

"""

# 7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de una semana.
# • Calcular el promedio de las mínimas y el de las máximas.
# • Mostrar en qué día se registró la mayor amplitud térmica.

"""matriz = [
    [8,20],
    [7,18],
    [10,21],
    [9,19],
    [13,23],
    [15,25],
    [14,24]
]
promedio_min = 0
promedio_max = 0
mayor_amplitud = 0
dia_amplitud = 0

for i, temp in enumerate(matriz):
    minima = temp[0]
    maxima = temp[1]
    promedio_min += minima
    promedio_max += maxima

    amplitud = maxima - minima
    if amplitud > mayor_amplitud:
        mayor_amplitud = amplitud
        dia_amplitud = i

promedio_min = promedio_min // len(matriz)
promedio_max = promedio_max // len(matriz)


print(f"El promedio de la maxima es de: {promedio_max: .2f}")
print(f"El promedio de la minima es de: {promedio_min: .2f }")
print(f"La mayor amplitud fue de {mayor_amplitud} el dia {dia_amplitud+1}")"""

# 8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# • Mostrar el promedio de cada estudiante.
# • Mostrar el promedio de cada materia.

"""matriz = [
    [8,6,7],
    [10,8,9],
    [10,7,7],
    [9,7,8],
    [8,8,6]
]
primer_materia = 0
segunda_materia = 0
tercer_materia = 0
cant_alumno = 5"""

"""for i, notas_aulumno in enumerate(matriz):
    promedio = 0
    for nota in notas_aulumno:
        promedio += nota
    print(f"El promedio del alumno N°{i+1} es de: {promedio/3}")"""

"""for i in matriz:
    primer_materia += i[0]
    segunda_materia += i[1]
    tercer_materia += i[2]

print(f"El promedio de la primer materia es de: {primer_materia/cant_alumno:.2f}")
print(f"El promedio de la segunda materia es de: {segunda_materia/cant_alumno:.2f}")
print(f"El promedio de la tercer materia es de: {tercer_materia/cant_alumno:.2f}")"""

# 9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# • Inicializarlo con guiones "-" representando casillas vacías.
# • Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# • Mostrar el tablero después de cada jugada.

"""tateti = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

print("---Bienvenido a la partida de TA-TE-TI---",end="\n\n")
for fila in tateti:
    print(" ".join(fila))

turno = "X"

#Creamos un bucle while para que los jugadores posicionen la "X" Y el "O"
while True:
    print(f"\nTurno del jugador {turno}")
    jugada = input("Ingresa fila y columna (ejemplo: 1 3): ")

    partes = jugada.split()

    #Verificamos que el jugador haya puesto 2 valores
    if len(partes) != 2:
        print("Debes ingresar DOS números: fila y columna.")
        continue
    
    #Verificamos que el jugador haya ingresado numeros y no otra cosa
    if not (partes[0].isdigit() and partes[1].isdigit()):
        print("Debes ingresar solo números.")
        continue
    
    # Ubicamos esos digitos en su respectiva fila y columna
    fila = int(partes[0]) - 1
    col  = int(partes[1]) - 1
    
    # Validamos que los rangos sean validos
    if not (0 <= fila < 3 and 0 <= col < 3):
        print("Posición fuera de rango (solo entre 1 y 3).")
        continue
    
    # Validamos que el casillero es vacio
    if tateti[fila][col] != "-":
        print("Casillero ocupada, intenta otra vez.")
        continue
    
    # Finalmente completamos la jugada
    tateti[fila][col] = turno
    
    # Mostramos el tablero actualizado luego de la jugada
    for fila_tablero in tateti:
        print(" ".join(fila_tablero))
    
    # Verificamos si hay algun jugador que haya coincidido en alguna fila y asi anunciarlo ganador
    for f in tateti:
        if f[0] == f[1] == f[2] != "-":
            print(f"\n🎉 ¡Jugador {turno} ha ganado!")
            exit()
    
     # Verificamos si hay algun jugador que haya coincidido en alguna columna y asi anunciarlo ganador
    for c in range(3):
        if tateti[0][c] == tateti[1][c] == tateti[2][c] != "-":
            print(f"\n🎉 ¡Jugador {turno} ha ganado!")
            exit()
    
    # Verificamos si hay algun jugador que haya coincidido en alguna diagonal y asi anunciarlo ganador
    if tateti[0][0] == tateti[1][1] == tateti[2][2] != "-" or tateti[0][2] == tateti[1][1] == tateti[2][0] != "-":
        print(f"\n🎉 ¡Jugador {turno} ha ganado!")
        exit()
    
     # Verificar si hay algun empate
    lleno = True
    for f in tateti:
        for c in f:
            if c == "-":
                lleno = False
                
    if lleno:
        print("\n Hay un empate, no hay mas casillas.")
        exit()
    
    # Aqui cambiamos los turnos de los jugadores
    if turno == "X":
        turno = "O"
    else:
        turno = "X"""

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# • Mostrar el total vendido por cada producto.
# • Mostrar el día con mayores ventas totales.
# • Indicar cuál fue el producto más vendido en la semana.


matriz = [
    ["Pera", "Pera", "Pera", "Pera", "Pera", "-", "Pera"],       
    ["Manzana", "Manzana", "-", "Manzana", "Manzana", "Manzana", "Manzana"],  
    ["Banana", "-", "Banana", "-", "Banana", "Banana", "Banana"],  
    ["-", "-", "-", "-", "-", "-", "-"]                       
]

cant_pera = 0
cant_manza = 0
cant_bana = 0

for i, fila in enumerate(matriz):
    for producto in fila:
        if producto == "Pera":
            cant_pera += 1
        elif producto == "Manzana":
            cant_manza += 1
        elif producto == "Banana":
            cant_bana += 1


print(f"--- Total venta ---")
print(f"\nSe vendieron {cant_pera} de Pera.")
print(f"\nSe vendieron {cant_manza} de Manzanas.")
print(f"\nSe vendieron {cant_bana} de Bananas.")


# A continuacion calculamos y luego mostramos el dia con mayor venta:
total_por_dia = []

# Calcular total vendido por cada día

for col in range(7):   
    total = 0
    for fila in range(4):  
        if matriz[fila][col] != "-":
            total += 1
    total_por_dia.append(total)

# Buscar el día o los dias con mayor venta
maxima_venta = max(total_por_dia)
dias_max_venta = []

for i in range(len(total_por_dia)):
    if total_por_dia[i] == maxima_venta:
        dias_max_venta.append(i + 1)  

print(f"\nLos dias con mayor venta son: {dias_max_venta} con {maxima_venta} productos vendidos")

#Producto más vendido en la semana 
max_ventas_producto = max(cant_pera, cant_manza, cant_bana)
productos_mas_vendidos = []

if cant_pera == max_ventas_producto:
    productos_mas_vendidos.append("Pera")
if cant_manza == max_ventas_producto:
    productos_mas_vendidos.append("Manzana")
if cant_bana == max_ventas_producto:
    productos_mas_vendidos.append("Banana")

print(f"\nEl/Los producto/s más vendido/s en la semana: {', '.join(productos_mas_vendidos)}  con {max_ventas_producto} unidades")