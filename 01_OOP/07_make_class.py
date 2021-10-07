# https://www.codewars.com/kata/5d774cfde98179002a7cb3c8/python

# I don't like writing classes like this:

# class Animal:
#     def __init__(self, name, species, age, health, weight, color):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.health = health
#         self.weight = weight
#         self.color = color
# Give me the power to create a similar class like this:

# Animal = make_class("name", "species", "age", "health", "weight", "color")


def make_class(*args: str):
    """fuction takes list of attributes and creates class with those attributes"""
    attributes = {k: k for k in args}
    return type("Animal", (), attributes)
