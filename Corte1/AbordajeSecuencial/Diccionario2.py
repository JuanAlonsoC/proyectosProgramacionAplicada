#Juan David Alonso - 20241005062
#### Obtener un valor con su clave
# un diccionario guarda información con pares clave: valor
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
print(building_heights["Burj Khalifa"])  # imprime 828
print(building_heights["Ping An"])       # imprime 599

# otro ejemplo con signos del zodiaco
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])


## Obtener una clave que no existe
# esto da error porque esa clave no está en el diccionario
# print(building_heights["Landmark 81"])

# forma segura: primero reviso si la clave está
key_to_check = "Landmark 81"
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

# agrego una nueva clave al diccionario
zodiac_elements["energy"] = "Not a Zodiac element"

if "energy" in zodiac_elements:
  print(zodiac_elements["energy"])


## Obtener con .get()
# .get() devuelve el valor si existe o None si no está
print(building_heights.get("Shanghai Tower"))  # devuelve 632
print(building_heights.get("My House"))        # devuelve None

# ejemplo con usuarios
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
print(user_ids.get("teraCoder"))

# si la clave existe tomo su valor, si no le pongo uno por defecto
if user_ids.get("teraCoder") == None:
   tc_id = 1000
else: 
   tc_id = user_ids.get("teraCoder")
print(tc_id)

if user_ids.get("superStackSmash") == None:
     stack_id = 100000
print(stack_id)


### Borrar una clave
# con .pop() puedo borrar algo del diccionario usando la clave
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
print(raffle.pop(320291, "No Prize"))  # saca Gift Basket
print(raffle)

print(raffle.pop(100000, "No Prize"))  # si no existe devuelve "No Prize"
print(raffle)

print(raffle.pop(872921, "No Prize"))  # saca Concert Tickets
print(raffle)

# ejemplo con juego
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)  # sumo el valor de stamina grains
health_points += available_items.pop("power stew", 0)      # sumo power stew
health_points += available_items.pop("mystic bread", 0)    # como no existe suma 0

print(available_items)
print(health_points)


## Obtener todas las claves
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
print(list(test_scores))   # muestra solo las claves

for student in test_scores.keys():
  print(student)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


## Obtener todos los valores
for score_list in test_scores.values():
  print(score_list)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)


## Obtener todos los pares clave-valor
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
for company, value in biggest_brands.items():
  print(company + " tiene un valor de " + str(value) + " billones de dólares")

pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for occupation, percentage in pct_women_in_occupation.items():
  print("Las mujeres son el " + str(percentage) + "% de los " + occupation + "s")
