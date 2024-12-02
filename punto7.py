def evaluar_estudiante(nombre, asignatura, calificacion):
    if calificacion >=7:
        print(nombre, "ha aprobado la asignatura", asignatura, "con una calificacion de", calificacion)
    else:
        print(nombre, "ha reprobado la asignatura", asignatura, "con una calificacion de", calificacion)

nombre = input("Digite el nombre del estudiante: ")
asignatura = input("Digite la asignatura: ")
calificacion = float(input("Digite la nota del estudiante (del 1 al 10): "))

evaluar_estudiante(nombre, asignatura, calificacion)