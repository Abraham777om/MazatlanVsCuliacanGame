class Person:
    def __init__(self, name, lastname, age, skin):
        self._name = name
        self._lastname = lastname
        self._age = age
        self._skin = skin

    def greet(self):
        return f'Hello! my name is {self._name} {self._lastname} I am {self._age} years old and my face is {self._skin}'

    def like(self, hobbie):
        self._hobbie = hobbie
        return f'Hi I am {self._name} and I like {self._hobbie}'

person1 = Person("Gibran", "Soto", 19, "brown")
print(person1.greet())
print(person1._name)

print(person1.like("Fortnite"))

class Dog:
    def __init__(self, name, age, race):
        self.__name = name
        self.__age = age
        self.__race = race

    def bark(self):
        return f'{self.__name} I am a dog and I make woof woof'

dog1 = Dog("Zeus", 5, "Doberman")
print(dog1.bark())
#print(dog1.__name)

# Python program demonstrate
# abstract base class work
from abc import ABC, abstractmethod

class Car(ABC):
    def mileage(self):
        pass

class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")

class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")

class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")

class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code
t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

class Student(Person):
    def __init__(self, name, lastname, age, skin, school, gradePoint):
        self._school = school
        self._gradePoint = gradePoint
        super().__init__(name, lastname, age, skin)

    def school(self):
        return f'Student: {self._name} School: {self._school}'

    def grade(self):
        return f'Student: {self._name} Grade Point: {self._gradePoint}'

student1 = Student("Edú", "Monárrez", 19, "white", "UNIPOLI", 9.8)
print(student1.greet())
print(student1.school())
print(student1.grade())


class Narco():
    def kill(self):
        return f'A narco kills'

class Puntero(Narco):

    def kill(self):
        return f'A puntero kills with a pistol'

class Sicario(Narco):

    def kill(self):
        return f'A Sicario torture and kills with machete'

narco1 = Narco()
puntero1 = Puntero()
sicario1 = Sicario()

print(narco1.kill())
print(puntero1.kill())
print(sicario1.kill())
