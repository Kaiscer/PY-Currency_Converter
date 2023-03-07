"""
Crea otra Clase llamada Perro que va a heredar de la clase Mascota, para poder ver este
comportamiento particular en diferentes perros (objetos Perro).
"""
from Pet import Pet


class Dog(Pet):
    def __init__(self, name, age, chase_cats):
        super().__init__(name, "Dog", age)
        self.chase_cats = chase_cats

    def __chase_Cats__(self):
        if self.chase_cats:
            print("%s persigue gatos" % self.name)
        else:
            print("%s no persigue gatos" % self.name)


tobi = Dog("Tobi", 3, True)
persi = Pet("Persi", "Gato", 1)
moli = Dog("Moli", 2, False)
cani = Pet("Cani", "Canario", 4)
anki = Pet("Anki", "Gato", 2)
chuski = Dog("Chuski", 3, True)

pets = [tobi, persi, moli, cani, anki, chuski]

print("Todas las mascotas:")
for pet in pets:
    print(pet)

print("\n")

print("Información completa de los gatos:")
for pet in pets:
    if pet.see_species() == "Gato":
        print("%s es un %s y tiene %d años" % (pet.see_name(), pet.see_species(), pet.see_age()))

print("\n")

print("Mascota más vieja:")
oldestPet = pets[0]
for pet in pets:
    if pet.see_age() > oldestPet.see_age():
        oldestPet = pet

print("%s es el/la %s más viejo/a y tiene %d años" % (oldestPet.see_name(),
                                                      oldestPet.see_species(), oldestPet.see_age()))

print("\n")

tobi.__chase_Cats__()
moli.__chase_Cats__()
chuski.__chase_Cats__()