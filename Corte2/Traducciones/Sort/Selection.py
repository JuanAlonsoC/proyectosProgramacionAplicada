def selection_sort(arr):
    n = len(arr)

    # Itera hasta el penúltimo elemento
    for i in range(n - 1):
        min_index = i  # Asume que el menor está en la posición i

        # Busca el menor en el resto del arreglo (parte desordenada)
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Si se encontró un nuevo menor, se intercambia con el elemento actual
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

def print_array(arr):
    # Imprime los elementos separados por espacio
    print(*arr)

if __name__ == "__main__":
    arr = [5, 3, 6, 1, 4]
    
    # n no es necesario pasarlo en Python, se calcula dentro con len(arr)
    n = len(arr)

    print("Arreglo original:")
    print_array(arr)

    selection_sort(arr)

    print("Arreglo ordenado:")
    print_array(arr)
