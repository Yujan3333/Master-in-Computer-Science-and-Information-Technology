# Parent class
class Animal:
    '''Parent Class accepts name and sound'''
    def __init__(self, name, sound):
        self.name = name       # Public attribute
        self._species = "Unknown"  # Protected attribute
        self.__sound = sound   # Private attribute

    def make_sound(self):
        return f"{self.name} makes a {self.__sound} sound."

    def get_species(self):
        return self._species  # Accessing protected attribute

# Child class (Inheritance)
class Dog(Animal):
    '''Child Class takes Dog name and breed'''
    def __init__(self, name, breed):
        super().__init__(name, "bark")  # Calling parent constructor for sound
        self._species = "Canine"  # Modifying protected attribute for species
        self.breed = breed  # Dog Class new attribute

    # Overriding method (Polymorphism)
    def make_sound(self):
        return f"{self.name} ({self.breed}) barks."

# Another child class (Polymorphism)
class Cat(Animal):
    '''Child class takes Cat name'''
    def __init__(self, name):
        super().__init__(name, "meow")
        self._species = "Feline"

    def make_sound(self):
        return f"{self.name} meows."

# Creating objects of Dog and Cat Class
dog = Dog("Ghost", "Golden Retriever")
cat = Cat("Mighty")

# Accessing public, protected, and private data
print(dog.make_sound())  # Polymorphism
print(cat.make_sound())  # Plymorphism

print(f"{dog.name} belongs to species: {dog.get_species()}")  # Accessing protected attribute
print(f"{cat.name} belongs to species: {cat.get_species()}")

# Encapsulation (trying to access private variable directly)
try:
    print(dog.__sound)  
except AttributeError:
    print("Cannot access private attribute '__sound' directly! Encapsulation")
