cantidad = int(input("Cantidad de números: "))

numeros = []

for i in range(cantidad):
    numero = int(input("Ingrese un número: "))
    numeros.append(numero)

for i in range(cantidad):
    for j in range(i + 1, cantidad):
        if numeros[i] > numeros[j]:
            aux = numeros[i]
            numeros[i] = numeros[j]
            numeros[j] = aux

print("El segundo número mayor es:", numeros[cantidad - 2])