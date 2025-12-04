def insertion_sort(arr):
    n = len(arr)

    # Comienza desde el segundo elemento (el elemento en índice 0 se considera ya ordenado)
    for i in range(1, n):
        key = arr[i]  # Valor a insertar
        j = i - 1

        # Mueve los elementos de arr[0..i-1] que son mayores que key
        # a una posición adelante de su posición actual
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Inserta la key en la posición correcta
        arr[j + 1] = key

def print_array(arr):
    # Imprime los elementos separados por un espacio
    print(*arr)

if __name__ == "__main__":
    arr = [5, 2, 4, 6, 1]
    
    # Calculamos el tamaño solo para mostrarlo, el algoritmo usa len(arr) internamente
    n = len(arr)

    print("Arreglo original:")
    print_array(arr)

    insertion_sort(arr)

    print("Arreglo ordenado:")
    print_array(arr)
