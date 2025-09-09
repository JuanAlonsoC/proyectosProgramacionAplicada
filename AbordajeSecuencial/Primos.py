# Este ejercicio vale una decima del primer corte
while True:
    v = input("Ingrese un número: ")
    v = int(v)

    cont = 0
    for n in range(1, v + 1):
        rsd = v % n
        if rsd == 0:
            cont = cont + 1

    if cont == 2:
        print(f'{v} es un número primo\n')
    else:
        print(f'{v} NO es un número primo\n')
