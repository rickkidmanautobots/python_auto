from typing import List


class Animal:
    def __init__(self, name):
        self.animalName = name

    def vocalize(self):
        print(f'{self.animalName} made a sound')


class Toy:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
        self.has_ball = False
        self.toys: List[Toy] = []

    def fetch(self, toy: Toy):
        self.toys.append(toy)
        print(f'{self.animalName} fetched the {toy.name}')
        self.has_ball = True

    def vocalize(self):
        print(f'{self.animalName} barked')

    def print_toys(self):
        for toy in self.toys:
            print(toy.name)


# sock = Toy('sock')
# ball = Toy('ball')
# rope = Toy('rope')

dog = Dog('Dizzy')
dog.vocalize()
dog.fetch(Toy('sock'))
dog.fetch(Toy('ball'))
dog.fetch(Toy('rope'))
dog.print_toys()

animal = Animal('Dog')
animal.vocalize()


