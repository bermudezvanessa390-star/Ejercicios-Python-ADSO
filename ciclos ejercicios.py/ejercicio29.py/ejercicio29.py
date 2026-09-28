#ciclos

numero = int(input("Número: "))

contador = 0

for i in range(1, numero + 1):
    if numero % i == 0:
        contador = contador + 1

if contador == 2:
    print("El número", numero, "es primo.")
else:
    print("El número", numero, "no es primo.")