#1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.

"""for num in range(0,101):
    print (num)
"""
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de ígitos que contiene.

"""num = abs(int(input("Escriba un numero por favor: ")))
digitos = 0
if num != 0:
    while num > 0 :
        num = num // 10
        digitos += 1
    print(f"El numero tiene {digitos} digitos.")
else:
    print("Tu numero tiene 1 digito.")"""

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.

"""num1 = int(input("Ingrese el primer numero por favor: "))
num2 = int(input("Ingrese el segundo numero por favor: "))
menor = min(num1,num2)
mayor = max(num1,num2)
acumulador = 0

if num1 != num2:
    for i in range(menor+1,mayor):
        acumulador = acumulador + i
    print(f"La sumatoria entre {menor} y {mayor} es igual a: {acumulador}")
else:
    print("Elija dos numero diferente. Intentelo nuevamente")
"""
# 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

"""num = int(input("Ingrese un numero: "))
acumulador = 0

if num == 0:
    print("Ingresaste el cero, por lo tanto no hay sumas secuenciales.")
else:
    while num != 0:
        acumulador += num
        num = int(input("Ingrese otro numero (Ingrese 0 para detener el programa): "))
    print(f"La sumatoria de todos sus numeros da como resultado: {acumulador}")"""

#Tambien se puede realizar con un while true: 
"""acumulador = 0

while True:
    num = int(input("Ingrese un numero por favor (Ingrese 0 para detern el programa): "))
    if num == 0:
        break
    acumulador += num

print(f"La sumatoria de todos sus numeros da como resultado: {acumulador}")"""

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""import random

numero_adivinar = random.randint(0,9)
intentos = 0

while True:
    num = int(input("Ingrese un numero del 0 al 9: "))
    intentos += 1
    if num == numero_adivinar:
        print(f"Acertaste! Tus intentos fueron : {numero_adivinar}")
        break
    else:
        print("No acertaste. Intentelo nuevamente.")"""

# 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.
"""for num in range(100,-1,-2):
    print(num)"""

# 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario

"""num = int(input("Indique un numero: "))
sumatoria = 0

if num != 0:
    for i in range(0,num+1):
        sumatoria += i
    print(f"La sumatoria de los numeros entre el 0 y {num} es igual: {sumatoria}")
else:
    print("Elegi un número diferente a 0. Intentelo nuevamente.")"""

# 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

"""contador = 1
num_par = 0
num_impar = 0
num_neg = 0
num_pos = 0

while contador <= 100:  # Cambiando el numero 100 podemos cambiar la cantidad de numeros a procesar.
    num = int(input(f"Ingrese un numero ({contador}/5): "))
    contador += 1

    # Positivo / Negativo
    if num < 0:
        num_neg += 1
    elif num > 0:
        num_pos += 1

    # Par / Impar
    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

print(f"Los numeros positivos son: {num_pos}")
print(f"Los numeros negativos son: {num_neg}")
print(f"Los numeros pares son: {num_par}")
print(f"Los numeros impares son: {num_impar}")"""

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

"""num_variable = 100 # Cambiando el numero 100 podemos cambiar la cantidad de numeros a procesar.
sumatoria = 0

for i in range(num_variable):
    num = int(input("Ingrese un numero por favor: "))
    sumatoria += num

print(f"La media de los numeros que ingresaste es {sumatoria/num_variable}")"""

# 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

numero_invertido = 0
num = int(input("Insertar numero para invertir: "))

if num < 0:
    negativo = True
    num = abs(num)


while num != 0:
    digito = num % 10
    numero_invertido = numero_invertido * 10 + digito
    num //= 10

# Restauramos el signo si era negativo con la bandera hecha anteriormente
if negativo:
    numero_invertido *= -1

print(f"El número invertido es: {numero_invertido}")
