
cantidad = int(input("Cantidad de estudiantes: "))
estudiantes = {}

for i in range(cantidad):
    nombre = input("Nombre: ")
    nota = float(input("Nota: "))

    estudiantes[nombre] = nota

mejor_estudiante = "" 
mejor_nota = 0

for nombre in estudiantes:
    if estudiantes[nombre] > mejor_nota:
        mejor_nota = estudiantes[nombre]
        mejor_estudiante = nombre


print("El estudiante con la mejor nota es:")
