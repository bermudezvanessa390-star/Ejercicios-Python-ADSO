
frase=input("frase")
frase = input("Frase: ")
palabras = frase.split()

contador= {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] = contador[palabra] + 1

    else:
        contador[palabra] = 1
for palabra in contador:
    print(palabra, ":", contador[palabra])

                

