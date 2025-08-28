# 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

"""edad = int(input("Indique su edad por favor: "))

if edad < 18 : 
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")"""


# 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”

"""resultado_examen = int(input("Que resultado obtuvc en el examen? (1 al 10):  "))

if resultado_examen >= 6:
    print("Aprobado")
else: 
    print("Desaprobado")"""

# 3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar.

"""numero = int(input("Por favor ingrese un numero Par: "))

if numero % 2 != 0 :
    print("Por favor, ingrese un número par")
else:
    print("Ha ingresado un número par")"""

# 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

"""edad = int(input("Indique su edad por favor: "))

if edad <= 0:
    print("Has ingresado cero o un valor inválido, intente nuevamente.")
elif edad < 12:
    print("Tu categoría pertenece a: Niño/a")
elif 12 <= edad < 18:
    print("Tu categoría pertenece a: Adolescente")
elif 18 <= edad < 30:
    print("Tu categoría pertenece a: Adulto/a joven")
else: 
    print("Tu categoría pertenece a: Adulto/a")"""

#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string.

"""contraseña = input("Ingrese una contraseña que tenga entre 8 y 14 caracteres: ")

if 8 <= len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
"""
# 6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

"""import random
from statistics import mode, median, mean

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)


print("Números aleatorios:", numeros_aleatorios)
print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)


if moda == mediana == media:
    print("Sin sesgo: la media, la mediana y la moda son iguales")
elif media > mediana and mediana > moda:
    print("Sesgo positivo o a la derecha: la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda.")
elif media < mediana and mediana < moda:
    print("Sesgo negativo o a la izquierda: la media es menor que la mediana y, a su vez, la mediana es menor que la moda.")
else:
    print("Distribución asimétrica compleja: no encaja exactamente en sesgo positivo o negativo")"""


# 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

"""frase = input("Escriba un frase por favor: ").lower()
vocal = ["a","e","i","o","u"]

if  len(frase) != 0:
    if frase[-1] in vocal:
        print(f"{frase.capitalize()}!")
    else:
        print(frase.capitalize())
else:
    print("No escribiste nada. Intentelo nuevamente.")"""


#8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
""" 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
    2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
    3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.

El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

"""print("---MENU---")

nombre = input("Ingrese su Nombre por favor: ")

if len(nombre) != 0:
    print("1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO")
    print("2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
    print("3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")

    opcion = int(input("Ingrese la Opcion por favor: "))
    
    if opcion == 1:
        print(f"Su nombre queda en: {nombre.upper()}")
    elif opcion == 2:
        print(f"Su nombre queda en: {nombre.lower()}")
    elif opcion == 3:
        print(f"Su nombre queda en:{nombre.title()}")
    else:
        print("Opcion incorrecta. Debe elegir 1,2 o 3. Intentelo nuevamente.")
else:
    print("No escribiste nada. Intentelo nuevamente")"""

# 9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla:
""" ● Menor que 3: "Muy leve" (imperceptible).
    ● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
    ● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
    ● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
    ● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
    ● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

"""magnitud_terremoto = float(input("Indique la magnitud del terremoto: "))

if magnitud_terremoto < 0:
    print("La magnitud del terremoto no puede ser menor que 0")
elif magnitud_terremoto < 3:
    print("'Muy leve'. (imperceptible)")
elif 3 <= magnitud_terremoto < 4:
    print("'Leve'. (ligeramente perceptible)")
elif 4 <= magnitud_terremoto < 5:
    print("'Moderado'. (sentido por personas, pero generalmente no causa daños)")
elif 5 <= magnitud_terremoto < 6:
    print("'Fuerte'. (puede causar daños en estructuras débiles)")
elif 6 <= magnitud_terremoto < 7:
    print("'Muy Fuerte'. (puede causar daños significativos)")
else:
    print("'Extremo'. (puede causar graves daños a gran escala).")"""

# 10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. (Ver la tabla)

hemisferio = input("En qué hemisferio se encuentra (NORTE/SUR): ").upper()
mes = int(input("Ingrese el número de mes (1-12): "))
dia = int(input("Ingrese el día del mes: "))

if hemisferio not in ["NORTE", "SUR"]:
    print("Hemisferio inválido.")
else:
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion_norte = "Invierno"
        estacion_sur = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion_norte = "Primavera"
        estacion_sur = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion_norte = "Verano"
        estacion_sur = "Invierno"
    else:
        estacion_norte = "Otoño"
        estacion_sur = "Primavera"

    if hemisferio == "NORTE":
        print(f"En el hemisferio norte es {estacion_norte}.")
    else:
        print(f"En el hemisferio sur es {estacion_sur}.")
