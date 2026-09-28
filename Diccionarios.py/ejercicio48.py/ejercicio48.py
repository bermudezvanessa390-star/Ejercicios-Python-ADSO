cantidad = int(input("Cantidad de libros: "))

libros = {}

for i in range(cantidad):
    codigo = input("Código: ")
    titulo = input("Título: ")

    libros[codigo] = titulo

consultar = input("Consultar código: ")

if consultar in libros:
    print("Libro:", libros[consultar])
else:
    print("El código no existe")