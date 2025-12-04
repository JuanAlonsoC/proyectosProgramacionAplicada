def bubble_sort(arr):
    n = len(arr)
    
    # FOR EXTERNO: Recorre toda la lista
    # Equivale a: for (i = 0; i < n - 1; i++)
    for i in range(n - 1):
        
        # FOR INTERNO: Los últimos i elementos ya están ordenados,
        # así que no necesitamos revisarlos de nuevo.
        # Equivale a: for (j = 0; j < n - i - 1; j++)
        for j in range(0, n - i - 1):
            
            # CONDICIÓN DE INTERCAMBIO
            if arr[j] > arr[j + 1]:
                
                # --- TRUCO PYTHON ---
                # En C se usa una variable 'temp'.
                # En Python podemos hacer "Tuple Unpacking" para intercambiar en una línea:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Función auxiliar para imprimir (opcional en Python, pero útil para comparar)
def print_array(arr):
    # Imprime la lista separada por espacios
    print(*arr)


# --- Bloque Principal ---
if __name__ == "__main__":
    arr = [5, 1, 4, 2, 8]
    n = len(arr)
    
    print(f"Tamaño del arreglo: {n}")

    print("Arreglo original:")
    print_array(arr)

    # Llamamos a la función.
    # Al igual que en C, las listas se pasan por referencia,
    # así que 'arr' se modificará directamente.
    bubble_sort(arr)

    print("Arreglo ordenado:")
    print_array(arr)
