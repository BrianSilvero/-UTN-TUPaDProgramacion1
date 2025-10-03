import math
# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

# Definicion de funciones

"""def imprimir_hola_mundo():
    print("Hola Mundo!")


# Programa principal
imprimir_hola_mundo()"""

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario

"""# Definicion de funciones
def saludar_usuario(nombre):
    return f"Hola {nombre}!"


# Programa principal
nombre_de_usuario = input("Dime tu nombre: ")
if nombre_de_usuario.strip() == "":
    print("No escribiste tu nombre")
else:
    print(saludar_usuario(nombre_de_usuario))"""

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”.Pedir los datos al usuario y llamar a esta función con los valores ingresados.

"""# Definicion de funciones
def informacion_personal(nombre, apellido, edad, residencia):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}"


# Programa principal
nombre_de_usuario = input("Dime tu nombre: ")
apellido_de_usuario = input("Dime tu apellido: ")
edad_de_usuario = input("Dime tu edad: ")
residencia_de_usuario = input("Dime tu residencia: ")
print(informacion_personal(nombre_de_usuario, apellido_de_usuario, edad_de_usuario,residencia_de_usuario))"""

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

"""# Definicion de funciones
valor_de_pi = math.pi
def calcular_area_circulo(radio):
    return valor_de_pi * radio **2


def calcular_perimetro_circulo(radio):
    return 2 * valor_de_pi * radio

# Programa principal
radio = int(input("Indique el radio del circulo: "))

if radio < 0:
    print("El radio tiene que ser mayor a 0, intentelo nuevamente.")
else:
    print(f"El área del círculo es {calcular_area_circulo(radio):.2f} cm².")
    print(f"El perímetro del círculo es {calcular_perimetro_circulo(radio):.2f} cm.")"""


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

"""# Definicion de funciones

def segundos_a_horas(segundos):
    return segundos / 3600

# Programa principal

segundos = int(input("Indique los segundo a convertir en hora: "))

if segundos < 0 :
    print("El segundo tiene que ser mayor a 0.")
else:
    print(f"El pasaje de {segundos} segundos a horas, es de {segundos_a_horas(segundos):.2f} horas.")"""

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

"""# Definicion de funciones

def tabla_multiplicar(numero):
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

# Programa principal
numero = int(input("Indique un numero del 1 al 10: "))

if numero < 1 or numero > 10:
    print("Porf favor indicar un numero del 1 al 10. Intentelo nuevamente")
else:
    print(f"---La tabla del {numero} es---")
    tabla_multiplicar(numero)"""


#7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

"""# Definicion de funciones

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multip = a * b
    division = None if b == 0 else a / b
    return suma, resta, multip, division

# Programa principal

a = int(input("Indique el primer numero para realizar las operaciones: "))
b = int(input("Indique el segundo numero para realizar las operaciones: "))

suma, resta, multip, division = operaciones_basicas(a,b)

print(f"La Suma de {a} + {b} = {suma}")
print(f"La Resta de {a} - {b} = {resta}")
print(f"La Multiplicación de {a} * {b} = {multip}")
print(f"La Division de {a} / {b} = {division}")"""


# 8 Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

"""# Definición de funciones
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Programa principal
peso = float(input("Indique su peso en kilogramos: "))
altura = float(input("Indique su altura en metros: "))

if peso <= 0 or altura <= 0:
    print("El peso y la altura deben ser mayores a 0.")
else:
    imc = calcular_imc(peso, altura)
    print(f"Su IMC es: {imc:.2f}")"""


# 9 Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

"""# Definición de funciones
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Programa principal

temp_celsius = float(input("Indique el grado en Celsius: "))
print(f"La temperatura de {temp_celsius:.2f} °C es equivalente a {celsius_a_fahrenheit(temp_celsius):.2f} °Fahrenheit.")"""

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

# Definición de funciones

def calcular_promedio(a, b, c):
    return (a + b + c ) / 3

# Programa principal

a = float(input("Indicar el primer numero: "))
b = float(input("Indicar el segundo numero: "))
c = float(input("Indicar el tercer numero: "))

print(f"El promedio de los tres numero es: {calcular_promedio(a,b,c):.2f}.")