"""
Escribe un programa en Python llamado mascotas.py que contenga una Clase llamada Mascota que
permita crear mascotas con un nombre, una especie y una edad. La aplicación guardará toda la
información de las mascotas creadas.
En la Clase se definirán los métodos para ver el nombre ver_nombre(), ver la especie ver_especie(),
y ver la edad ver_edad(). Además, la Clase tendrá un método __str__ () que devolverá un mensaje del
tipo:    "%s es un %s" % (nombre, especie)
"""


class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def see_name(self):
        return self.name

    def see_species(self):
        return self.species

    def see_age(self):
        return self.age

    def __str__(self):
        return "%s es un %s" % (self.name, self.species)
