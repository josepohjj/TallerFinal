def factoriales(n):
    factorial = 1
    sumar = 0
    for i in range(1, n + 1): 
        factorial *= i 
        sumar += i
    promedio = sumar / n
    print("El factorial de", n, "es", factorial)
    print("La suma total del 1 al", n, "es", sumar)
    print("El promedio de", sumar, "y", n, "es", promedio)
n = int(input("Digite un valor: "))

factoriales(n)