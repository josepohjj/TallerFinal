def capital_anual(dinero, int_anual):
    return dinero + (dinero * int_anual / 100)


dinero = float(input("Cantidad de dinero a invertir: "))
int_anual = float(input("Interes anual del dinero invertido: ", )) 
capital = capital_anual(dinero, int_anual)

print("El capital obtenido despues de un año es de: ", capital)






""" dinero = float(input("Cantidad de dinero a invertir: "))
    int_anual = float(input("Interes anual del dinero invertido: ")) / 100
    capital = dinero * int_anual
    print("La inversion obtenida en el año ha sido de: ", capital) """