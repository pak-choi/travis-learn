
class Animal(object):
    def __init__(self, name):
        self._name = name
    def speek(self):
        raise NotImplementedError("I can't speek")
    

class Crow(Animal):
    def speek(self):
        print(f"I'm a crow called {self._name}. Caw.")


class Cat(Animal):
    def speek(self):
        print(f"I'm a cat called {self._name}. Meow.")


class Dog(Animal):
    def speek(self):
        print(f"I'm a dog called {self._name}. Woof.")