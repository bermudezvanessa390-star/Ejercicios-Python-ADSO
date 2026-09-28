cantidad = int(input("Cantidad de números: "))

numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

sin_repetidos = []

for numero in numeros:
    if numero not in sin_repetidos:
        sin_repetidos.append(numero)

print("Lista sin elementos repetidos:")

for numero in sin_repetidos:
    print(numero)