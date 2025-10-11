# 1) Dado el diccionario precios_frutas
# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':1450}
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300

"""precio_frutas = {
    'Banana': 1200,
    'Ananá': 2500,
    'Melón': 3000,
    'Uva': 1450 
}
precio_frutas['Naranja']= 1200
precio_frutas['Manzana']= 1500
precio_frutas['Pera']= 2300

print(precio_frutas)"""


#2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

"""precio_frutas['Banana']= 1330
precio_frutas['Manzana']= 1700
precio_frutas['Melón']= 2800
"""
#Tambien se puede realizar con la funcion update()
"""precio_frutas.update({
    'Banana': 1330,
    'Manzana': 1700,
    'Melón': 2800
})

print(precio_frutas)"""

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

"""lista_frutas = list(precio_frutas.keys())
print(lista_frutas)"""

# 4) Escribí un programa que permita almacenar y consultar números telefónicos. 
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

"""agenda = {}

# Funciones
def agendar(name, tel):
    agenda[name] = tel
    
contador = 0
while contador < 5:
    nombre = input("Indique un nombre: ").strip().capitalize()
    telefono = input("Indique el numero de telefono: ")
    agendar(nombre,telefono)
    contador += 1

print("\nAgenda cargada correctamente.")

consulta = input("\nIngrese un nombre para buscar su número: ").strip().capitalize()

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"No se encontró a {consulta} en la agenda.")"""

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

"""frase = input("Indique una frase: ").lower()
palabras = frase.split()

palabras_unicas = set(palabras)
recuento = {}
for palabra in palabras:
    recuento[palabra] = recuento.get(palabra,0) + 1

print("\nPalabras únicas:")
print(palabras_unicas)

print("\nRecuento de palabras:")
print(recuento)"""

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

"""alumnos = {}

for i in range(3):
    nombre = input("Indique el nombre del alumno: ").capitalize().strip()
    nota1= float(input("-Nota1 : "))
    nota2= float(input("-Nota2 : "))
    nota3= float(input("-Nota3 : "))
    notas = (nota1, nota2, nota3 )
    alumnos[nombre] = notas

for nombre,notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: promedio = {promedio:.2f}")"""

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2: 
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).


"""parcial1 = {"Ana", "Luis", "Sofía", "Carlos"}
parcial2 = {"Luis", "Sofía", "María", "Pedro"}

ambos = parcial1 & parcial2
solo_uno = (parcial1 - parcial2) | (parcial2 - parcial1)
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)"""

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
# Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe

"""stock = {
    "Manzanas": 50,
    "Peras": 30,
    "Bananas": 100
}

producto = input("Ingrese el nombre del producto: ").strip().capitalize()
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]} unidades.")
    nuevas = int(input("¿Cuántas unidades desea agregar? "))
    stock[producto] += nuevas
else:
    print(f"{producto} no está en el inventario.")
    nuevo_stock = int(input("Ingrese el stock inicial: "))
    stock[producto] = nuevo_stock

print("\nStock actualizado:")
print(stock)"""

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

"""agenda = {
    ("lunes", "11:00"): "Ir al medico",
    ("viernes","17:00"): "Ir a visitar la familia"
}
consulta = input("Que dia desea revisar en su agenda?(ej: lunes 11:00): ").strip().split()
dia = consulta[0].lower()
hora = consulta[1]
clave = (dia,hora)

if clave in agenda:
    print(f"Evento: {agenda[clave]}")
else:
    print("No hay eventos programados para ese horario.")"""


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
# diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Chile": "Santiago",
    "Uruguay": "Montevideo"
}
invertido = {
    
}

for key,value in paises.items():
    invertido[value] = key

print(invertido)