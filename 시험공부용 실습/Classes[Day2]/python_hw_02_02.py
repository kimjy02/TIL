class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('Woof!')

class Cat(Animal):
    def speak(self):
        print('Meow!')

class Flyer:
    def fly(self):
        print('Flying')

class Swimmer:
    def swim(self):
        print('Swimming')

class Duck(Flyer, Swimmer, Animal):
    def speak(self):
        print("Quack!")
    
    def fly(self):
        return super().fly()
    
    def swim(self):
        return super().swim()

def make_animal_speak(animal):
    animal.speak()

puppy = Dog('푸들')
kitty = Cat('샴')
donald = Duck('도날드덕')
make_animal_speak(puppy)
make_animal_speak(kitty)
make_animal_speak(donald)
donald.fly()
donald.swim()