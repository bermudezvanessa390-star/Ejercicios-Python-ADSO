cantidad = int(input("Cantidad de elementos: "))

lista1 = []
lista2 = []

print("Lista 1:")
for i in range(cantidad):
    numero = int(input())
    lista1.append(numero)

print("Lista 2:")
for i in range(cantidad):
    numero = int(input())
    lista2.append(numero)

lista3 = []

for numero in lista1:
    lista3.append(numero)

for numero in lista2:
    lista3.append(numero)

print("Lista combinada:")

for numero in lista3:
    print(numero)