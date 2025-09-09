# Este ejercicio vale una decima del primer corte
while True:
    n = input("Ingrese un número: ")
    n = int(n)
    rsd = n % 2
    if rsd == 0:
        print(str(n) + " es par")
    else:
        print(str(n) + " es impar")
