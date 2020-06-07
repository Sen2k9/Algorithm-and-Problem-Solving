
import unittest


class AnimalShelter:

    # constructor
    def __init__(self):
        self.cat = []
        self.dog = []

    def enqueue(self, animal):

        if animal.__class__ == Cat:
            self.cat.append(animal)

        else:

            self.dog.append(animal)

    def dequeueAny(self):

        if len(self.cat):
            return self.dequeueCat()

        return self.dequeueDog()

    def dequeueDog(self):

        if len(self.dog):
            dog = self.dog[0]

            self.dog = self.dog[1:]

            return dog

    def dequeueCat(self):

        if len(self.cat):

            cat = self.cat[0]

            self.cat = self.cat[1:]

            # print(cat)

            return cat


class Animal:  # animal class

    def __init__(self, name):

        self.name = name

    def __str__(self):

        return self.name


class Dog(Animal):  # dog class
    pass


class Cat(Animal):  # cat class
    pass


class Test(unittest.TestCase):

    def test_animal_shelter(self):

        shelter = AnimalShelter()

        shelter.enqueue(Cat("A"))
        shelter.enqueue(Cat("B"))
        shelter.enqueue(Dog("C"))
        shelter.enqueue(Dog("D"))
        shelter.enqueue(Cat("E"))

        self.assertEqual(str(shelter.dequeueAny()), "A")
        self.assertEqual(str(shelter.dequeueAny()), "B")
        self.assertEqual(str(shelter.dequeueDog()), "C")
        self.assertEqual(str(shelter.dequeueCat()), "E")
        self.assertEqual(str(shelter.dequeueAny()), "D")


if __name__ == "__main__":  # assign this namespace as main

    unittest.main()


# unittest.main()


"""
Ideal question for OOP questions
"""
