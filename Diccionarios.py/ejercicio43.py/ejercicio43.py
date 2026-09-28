
cantidad_productos = int(input("Cantidad de productos: "))

productos = {}

for i in range(cantidad_productos):
    producto = input("Producto: ")
    cantidad = int(input("Cantidad: "))

    productos[producto] = cantidad

consultar = input("Consultar producto: ")

if consultar in productos:
    print("Cantidad disponible de", consultar, ":", productos[consultar])
else:
    print("El producto no se encuentra en la lista.")