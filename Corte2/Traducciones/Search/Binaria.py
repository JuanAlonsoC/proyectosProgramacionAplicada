def first_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1  # aquí guardaremos la mejor posición encontrada

    while low <= high:
        # En Python se usa // para división entera
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid      # encontramos una ocurrencia
            high = mid - 1    # seguimos buscando MÁS A LA IZQUIERDA
        elif key < arr[mid]:
            high = mid - 1    # ir a la mitad izquierda
        else:
            low = mid + 1     # ir a la mitad derecha

    return result

def last_occurrence(arr, key):
    low = 0
    high = len(arr) - 1
    result = -1  # aquí guardaremos la mejor posición encontrada

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            result = mid      # encontramos una ocurrencia
            low = mid + 1     # seguimos buscando MÁS A LA DERECHA
        elif key < arr[mid]:
            high = mid - 1    # ir a la mitad izquierda
        else:
            low = mid + 1     # ir a la mitad derecha

    return result

# --- Bloque Principal (Main) ---
if __name__ == "__main__":
    # Arreglo de ejemplo: OJO, está ORDENADO
    arr = [3, 5, 7, 9, 11, 11, 11, 11, 13, 15]
    
    print("Arreglo (ordenado):", end=" ")
    for num in arr:
        print(num, end=" ")
    print() # Salto de línea

    try:
        key = int(input("Ingrese el numero a buscar: "))
        
        # En Python no hace falta pasar 'n' (tamaño), la lista ya sabe su tamaño
        first = first_occurrence(arr, key)
        last = last_occurrence(arr, key)

        if first == -1:
            print(f"El numero {key} NO se encuentra en el arreglo.")
        else:
            count = last - first + 1
            print(f"El numero {key} aparece {count} veces.")
            
            print("Posiciones (indices 0-based):", end=" ")
            # range en Python no incluye el último número, por eso es last + 1
            for i in range(first, last + 1):
                print(i, end=" ")
            print()
            
    except ValueError:
        print("Por favor, ingrese un número válido.")
