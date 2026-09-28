
cantidad = int(input("Cantidad de contactos: "))

agenda = {}

for i in range(cantidad):
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")

    agenda[nombre] = telefono

buscar = input("Buscar contacto: ")

print("Teléfono de", buscar, ":", agenda[buscar])