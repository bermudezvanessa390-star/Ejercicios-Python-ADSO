cantidad = int(input("Cantidad de estudiantes: "))

estudiantes = {}

for i in range(cantidad):
    codigo = input("Código: ")
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    carrera = input("Carrera: ")
    promedio = float(input("Promedio: "))

    estudiantes[codigo] = {
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "promedio": promedio
    }

mejor_estudiante = ""
mejor_promedio = 0

for codigo in estudiantes:
    if estudiantes[codigo]["promedio"] > mejor_promedio:
        mejor_promedio = estudiantes[codigo]["promedio"]
        mejor_estudiante = codigo

print("Mejor estudiante")
print("Código:", mejor_estudiante)
print("Nombre:", estudiantes[mejor_estudiante]["nombre"])
print("Edad:", estudiantes[mejor_estudiante]["edad"])
print("Carrera:", estudiantes[mejor_estudiante]["carrera"])
print("Promedio:", estudiantes[mejor_estudiante]["promedio"])