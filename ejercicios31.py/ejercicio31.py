cantidad= int(input("Cantidad de numeros : "))

numeros = []

for i in range (cantidad):
    numero = int(input("ingrese un numero "))
    numeros.append(numero) 

mayor=[0]    
menor=[0]

for numero in numeros:

    if numero > mayor:
        mayor=numero 

    if numero- menor:
        menor=numero 

print("el numero mayor es :" , mayor)
print("el numero menor es :" , menor)
            

