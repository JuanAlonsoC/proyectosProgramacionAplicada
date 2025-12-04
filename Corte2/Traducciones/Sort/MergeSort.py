def merge(arr, l, m, r):
    # Crea subarreglos temporales usando rebanadas (slicing) de Python
    # Esto reemplaza los bucles 'for' de copia del código en C
    # L corresponde a arr[l..m]
    L = arr[l : m + 1]
    # R corresponde a arr[m+1..r]
    R = arr[m + 1 : r + 1]

    # Índices iniciales para L (i), R (j) y el arreglo principal (k)
    i = 0
    j = 0
    k = l

    # Mezclar los arreglos temporales de vuelta en arr[l..r]
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar los elementos restantes de L, si los hay
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar los elementos restantes de R, si los hay
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        # Encuentra el punto medio (división entera)
        m = l + (r - l) // 2

        # Llamada recursiva para la primera mitad
        merge_sort(arr, l, m)
        # Llamada recursiva para la segunda mitad
        merge_sort(arr, m + 1, r)

        # Mezcla las dos mitades ordenadas
        merge(arr, l, m, r)

if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    # n es la longitud de la lista
    n = len(arr)

    # Llamada inicial con los índices extremos (0 y n-1)
    merge_sort(arr, 0, n - 1)

    print("Arreglo ordenado:")
    # Imprime los elementos separados por espacio
    print(*arr)
