cantidad = int(input("Cantidad de notas: "))

suma = 0

for i in range(cantidad):
    nota = float(input("Ingrese una nota: "))
    suma = suma + nota

promedio = suma / cantidad

print("El promedio de las notas es:", promedio)