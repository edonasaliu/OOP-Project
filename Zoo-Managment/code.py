class Animal:
    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def make_sound(self):
        pass

    def __str__(self):
        return f'{self.name}, {self.weight}kg, {self.age} years old'


class Lion(Animal):
    def __init__(self, name, weight, age, mane_size):
        super().__init__(name, weight, age)
        self.mane_size = mane_size

    def make_sound(self):
        return "Roar"


class Shark(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)

    def swim(self):
        return "Swimming"


class Giraffe(Animal):
    def __init__(self, name, weight, age):
        super().__init__(name, weight, age)


class Enclosure:
    def __init__(self, temperature_range, feeding_schedule):
        self.temperature_range = temperature_range
        self.feeding_schedule = feeding_schedule
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def __str__(self):
        animal_str = '\n'.join(str(animal) for animal in self.animals)
        return f'Enclosure with {len(self.animals)} animals:\n{animal_str}'


class SavannahEnclosure(Enclosure):
    def __init__(self):
        super().__init__((25, 31), "Daily")


class SharkEnclosure(Enclosure):
    def __init__(self):
        super().__init__((17, 18), "Weekly")


# Creating instances of animals
lion = Lion('Leo', 190, 5, 'Large')
shark = Shark('Sharky', 300, 10)
giraffe = Giraffe('Gerry', 800, 7)

# Creating instances of enclosures
savannah_enclosure = SavannahEnclosure()
shark_enclosure = SharkEnclosure()

# Adding animals to enclosures
savannah_enclosure.add_animal(lion)
savannah_enclosure.add_animal(giraffe)
shark_enclosure.add_animal(shark)

# Printing information about the enclosures
print('Savannah Enclosure:')
print(savannah_enclosure)
print('\nShark Enclosure:')
print(shark_enclosure)