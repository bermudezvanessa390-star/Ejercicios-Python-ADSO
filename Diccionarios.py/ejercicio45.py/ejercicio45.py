palabra = input("Palabra: ")

contador = {}

for letra in palabra:
    if letra in contador:

        contador[letra] = contador[letra] + 1

    else:
        contador[letra] = 1

for letra in contador:

    print(letra, ":", contador[letra])            