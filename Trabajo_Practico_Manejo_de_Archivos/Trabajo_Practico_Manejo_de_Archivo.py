# 1. Crear archivo inicial con productos: Crear un archivo de texto llamado productos.txt con tres productos. Cada línea debe tener: nombre,precio,cantidad.

with open("productos.txt", "w") as archivo:
    archivo.write("Pera,20,2\n")
    archivo.write("Manzana,15,5\n")
    archivo.write("Banana,10,8")

# 2. Leer y mostrar productos: Crear un programa que abra productos.txt, lea cada línea, la procese con .strip() y .split(","), y muestre los productos en el siguiente formato:
# Producto: Lapicera | Precio: $120.5 | Cantidad: 30

with open("productos.txt","r") as archivo:
    lineas = archivo.readlines()
    for linea in lineas:
        partes = linea.strip().split(",")
        print(f"Producto: {partes[0]} | Precio: ${partes[1]} | Cantidad: {partes[2]}")

# 3. Agregar productos desde teclado: Modificar el programa para que luego de mostrar los productos, le pida al usuario que ingrese un nuevo producto (nombre, precio, cantidad) y lo agregue al archivo sin borrar el contenido existente.

def agregar_productos(nombre, precio, cantidad):
    with open("productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"\n{nombre},{precio},{cantidad}")

while True:
    nombre = input("Indique el nombre del producto: ").strip()
    if not nombre:
        print("No se puede ingresar un nombre vacío. Inténtelo nuevamente.")
        continue

    while True:
        precio_str = input("Indique el precio del producto: ").strip()
        if not precio_str:
            print("No se puede dejar el precio vacío. Inténtelo nuevamente.")
            continue
        if not precio_str.isdigit():
            print("Debe ingresar solo números enteros. Inténtelo nuevamente.")
            continue

        precio = int(precio_str)
        if precio < 0:
            print("El precio no puede ser negativo. Inténtelo nuevamente.")
            continue
        break

    while True:
        cantidad_str = input("Indique la cantidad del producto: ").strip()
        if not cantidad_str:
            print("No se puede dejar la cantidad vacía. Inténtelo nuevamente.")
            continue
        if not cantidad_str.isdigit():
            print("Debe ingresar solo números enteros. Inténtelo nuevamente.")
            continue

        cantidad = int(cantidad_str)
        if cantidad < 0:
            print("La cantidad no puede ser negativa. Inténtelo nuevamente.")
            continue
        break

    agregar_productos(nombre, precio, cantidad)
    print(f"\nProducto agregado correctamente: {nombre}, ${precio}, cantidad {cantidad}\n")

    break

# 4. Cargar productos en una lista de diccionarios: Al leer el archivo, cargar los datos en una lista llamada productos, donde cada elemento sea un diccionario con claves: nombre, precio, cantidad.
productos = []
with open ("productos.txt","r") as archivo:
    for linea in archivo:
        nombre, precio, cantidad = linea.strip().split(",")
        diccionario = {
            'nombre' : nombre,
            'precio' : int(precio),
            'cantidad': int(cantidad)
        }
        productos.append(diccionario)

# 5  Buscar producto por nombre: Pedir al usuario que ingrese el nombre de un producto. Recorrer la lista de productos y, si lo encuentra, mostrar todos sus datos. Si no existe, mostrar un mensaje de error.

nombre_producto = input("Indique el nombre del producto a buscar: ").lower()
with open("productos.txt","r") as archivo:
    encontrado = False
    producto_encontrado = []
    for linea in archivo:
        partes = linea.strip().split(",")
        if partes[0].lower() == nombre_producto:
            encontrado = True
            producto_encontrado = partes
    if encontrado == False:
        print(f"No se encontro el producto '{nombre_producto}'")
    else:
        print(f"---Tu producto se ha encontrado con exito---")
        print(f"Producto: {producto_encontrado[0]} | Precio: ${producto_encontrado[1]} | Cantidad: {producto_encontrado[2]}")

# 6. Guardar los productos actualizados: Después de haber leído, buscado o agregado productos, sobrescribir el archivo productos.txt escribiendo nuevamente todos los productos actualizados desde la lista.

def guardar_productos(productos):
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for producto in productos:
            linea = f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n"
            archivo.write(linea)