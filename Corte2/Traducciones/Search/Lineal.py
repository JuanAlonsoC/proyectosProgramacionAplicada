def linear_search(arr, key):
    """
    Busca la primera aparición de key en arr.
    Devuelve el índice si lo encuentra, o -1 si no.
    """
    # range(len(arr)) genera números desde 0 hasta n-1
    # Esto equivale al for (int i=0; i<n; i++) de C
    for i in range(len(arr)):
        if arr[i] == key:
            return i  # Lo encontré, retorno la posición
            
    return -1  # Terminé el ciclo y no lo encontré


def linear_search_all(arr, key):
    """
    Busca TODAS las apariciones de key en arr.
    En Python, en lugar de pasar un arreglo vacío para llenar,
    es más común crear una lista y retornarla.
    """
    indices = []  # Lista dinámica (crece sola)
    
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)  # Agregamos el índice al final de la lista
            
    return indices  # Retornamos la lista completa de posiciones


# --- Bloque Principal ---
if __name__ == "__main__":
    arr = [4, 9, 2, 7, 5, 7, 9, 7]
    
    print("Arreglo:", end=" ")
    print(*arr) # El asterisco 'desempaqueta' la lista para imprimirla sin corchetes

    try:
        key_input = input("Ingrese el numero a buscar: ")
        key = int(key_input)

        # --- Búsqueda de una sola posición ---
        pos = linear_search(arr, key)

        if pos == -1:
            print(f"El numero {key} NO se encuentra en el arreglo.")
        else:
            print(f"El numero {key} se encuentra (al menos) en la posicion {pos} (indice 0-based).")

        # --- Búsqueda de todas las posiciones ---
        # En Python recuperamos la lista directamente
        found_indices = linear_search_all(arr, key)
        count = len(found_indices) # El tamaño de la lista es la cantidad de veces que apareció

        if count == 0:
            print(f"No se encontraron ocurrencias de {key}.")
        else:
            print(f"El numero {key} aparece {count} veces, en las posiciones:", end=" ")
            print(*found_indices)

    except ValueError:
        print("Error: Por favor ingrese un número entero válido.")
