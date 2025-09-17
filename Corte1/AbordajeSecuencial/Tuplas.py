#Juan David Alonso - 20241005062
#################LISTAS####################
###########################################

# creo una lista con varios colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

print(my_lista)              # imprime toda la lista
print(type(my_lista))        # muestra que el tipo de dato es list
print(my_lista[2])           # muestra el elemento en la posición 2 que es Amarillo

print("my_lista size: ", len(my_lista))   # muestra cuántos elementos tiene la lista
print(my_lista[0:2])         # muestra desde el elemento 0 hasta el 1
print(my_lista[:2])          # hace lo mismo de arriba pero escrito más corto

my_lista.append('Blanco')    # agrega Blanco al final
print(my_lista)

my_lista.insert(3, 'Negro')  # mete Negro en la posición 3 y corre los demás
print(my_lista)

my_lista.extend(['Marron', 'Gris'])   # pega otra lista al final
print(my_lista)

print(my_lista.index('Azul'))   # dice en qué posición está Azul

#my_lista.remove('Magenta')    # si el color no está en la lista da error
my_lista.remove('Marron')       # borra Marron
print(my_lista)

my_lista.insert(8, 'Marron')    # vuelve a meter Marron en la posición 8
print(my_lista)

print(my_lista.pop())           # saca el último de la lista y lo muestra
size = len(my_lista)
print("size = ", size)          # muestra el tamaño de la lista otra vez

# si multiplico una lista se repite varias veces
my_lista_3 = my_lista*3
print("my_lista_3: ", my_lista_3)

print("Sort:")
print()
my_listaSort = my_lista.sort()  # ordena la lista pero no devuelve nada
print(my_listaSort)             # por eso aquí sale None

# hago otra lista pero con números
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
my_NumList.sort()               # ordena de menor a mayor
print(my_NumList)

# también se puede ordenar de mayor a menor
my_NumList.sort(reverse = True)  
print("De menor a mayor: ", my_NumList)


#################TUPLAS####################
###########################################
# las tuplas se parecen a las listas pero aquí no se pueden cambiar los valores

# convierto la lista en tupla
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

print(my_tupla[0])   # muestra el primero
print(my_tupla[2])   # muestra el tercero

# se puede preguntar si un valor está en la tupla
print('Rojo' in my_tupla)      # true si está y false si no
print(my_tupla.count('Rojo'))  # cuenta cuántas veces está Rojo

# si quiero una tupla con un solo elemento tengo que poner una coma al final
my_tupla_unitaria = ('Blanco')   # aquí realmente es un string y no una tupla
print(my_tupla_unitaria)

# se puede crear una tupla sin paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# se puede guardar cada valor de la tupla en variables
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# también puedo volver la tupla una lista
my_lista2 = list(my_tupla)
print(my_lista2)