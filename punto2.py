def obtener_impares(ini, fin):
    for i in range(ini, fin + 1):
        if i % 2 != 0:
            print(i)

ini = int(input("Digite el rango inicial: "))
fin = int(input("Digite el rango final: "))

obtener_impares(ini, fin)