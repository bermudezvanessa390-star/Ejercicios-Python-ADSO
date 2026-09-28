
cantidad = int(input("Cantidad de vendedores: "))
vendedores = {}

for i in range(cantidad): 
    nombre = input("Nombre: ")
    ventas = int(input("Ventas: "))

    vendedores[nombre] = ventas

mayor_vendedor = ""
mayores_ventas = 0    

for nombre in vendedores: 
    if vendedores[nombre] > mayores_ventas: 
        mayores_ventas = vendedores[nombre]
        mayor_vendedor = nombre

print("Mayor vendedor:") 
print(mayor_vendedor, "-> $", mayores_ventas)        