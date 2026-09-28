cantidad = int(input("Cantidad de empleados: "))

empleados = {}

for i in range(cantidad):
    identificacion = input("Identificación: ")
    salario = float(input("Salario: "))

    empleados[identificacion] = salario

suma = 0

for identificacion in empleados:
    suma = suma + empleados[identificacion]

promedio = suma / cantidad

print("Salario promedio:", round(promedio, 2))