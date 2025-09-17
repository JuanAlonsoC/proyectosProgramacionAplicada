#Juan David Alonso - 20241005062
# un diccionario es como una lista pero en vez de posiciones usa "claves" para guardar un valor
# aquí cada cuarto tiene una temperatura
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
# aquí cada lugar tiene el número de cámaras
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
print(num_cameras)

# otro ejemplo con traducciones de palabras
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch" }
print(translations)

## probando un error
# aquí da error porque las listas no se pueden usar como clave en un diccionario
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
# print(powers)

# un diccionario con familias y los nombres de sus hijos
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"] , "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

# diccionario vacío
my_empty_dictionary = {}
print(my_empty_dictionary)

# ejemplo de un menú con precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["cheesecake"] = 8   # aquí agrego un nuevo plato al menú
print("After", menu)

# cambiando valores
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}   # al volver a asignar solo queda este último
print(animals_in_zoo)


## Agregar varias cosas de una sola vez
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

sensors.update({"pantry": 22, "guest room": 25, "patio": 34})  # agrego varias llaves de golpe
print("After", sensors)


# otro ejemplo con usuarios
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


## Sobrescribir valores
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)
menu["oatmeal"] = 5   # cambio el valor de una clave que ya existía
print("After", menu)

# más ejemplos con premios
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()
oscar_winners.update({"Supporting Actress": "Viola Davis"})  # agrego una nueva categoría
print("After1", oscar_winners)
print()
oscar_winners["Best Picture"] = "Moonlight"   # cambio el valor de Best Picture
print("After2", oscar_winners)


### Crear diccionarios con dos listas
# tengo una lista con nombres y otra con alturas
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# zip junta dos listas como si fueran pares
# zipStudents = zip(names, heights)
# print("zipStudents: ", zipStudents)

# aquí uso zip para crear un diccionario con nombre: altura
students = {key:value for key, value in zip(names, heights)}
print(students)

# otro ejemplo con bebidas y la cafeína
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

drinks_to_caffeine = {key:value for key, value in zipped_drinks}
print(drinks_to_caffeine)

# más ejemplos con canciones
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# creo el diccionario canción: veces escuchada
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)

# agrego una canción nueva
plays.update({"Purple Haze": 1})
# actualizo un valor que ya existía
plays.update({"Respect": 94})
print("After: ", plays)

# un diccionario dentro de otro
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
