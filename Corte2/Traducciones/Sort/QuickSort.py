def partition(arr, low, high):
    # Elegimos el último elemento como pivote (Esquema Lomuto)
    pivot = arr[high]
    
    # Índice del elemento más pequeño
    i = low - 1

    for j in range(low, high):
        # Si el elemento actual es menor que el pivote
        if arr[j] < pivot:
            i += 1
            # Intercambio de elementos
            arr[i], arr[j] = arr[j], arr[i]

    # Coloca el pivote en su posición correcta (después de los elementos menores)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    
    # Retorna la posición donde quedó el pivote
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
        # pi es el índice de partición, arr[pi] está ahora en el lugar correcto
        pi = partition(arr, low, high)

        # Ordena recursivamente los elementos antes y después de la partición
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def print_array(arr):
    # Imprime los elementos separados por un espacio
    print(*arr)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)

    print("Arreglo original:")
    print_array(arr)

    # Llamada inicial con los índices extremos (0 y n-1)
    quick_sort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    print_array(arr)
