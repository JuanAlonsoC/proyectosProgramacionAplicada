def bubble_sort(arr):
    n = len(arr)
    
    # Itera sobre todos los elementos del arreglo
    for i in range(n - 1):
        
        # Los últimos i elementos ya están ordenados en su posición final
        for j in range(0, n - i - 1):
            
            # Compara elementos adyacentes
            if arr[j] > arr[j + 1]:
                # Intercambia si el elemento actual es mayor que el siguiente
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def print_array(arr):
    # Imprime los elementos de la lista separados por espacio
    print(*arr)

if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    n = len(arr)
    
    print(f"Tamaño del arreglo: {n}")
    print("Arreglo original:")
    print_array(arr)

    bubble_sort(arr)

    print("Arreglo ordenado:")
    print_array(arr)
