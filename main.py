#!/usr/bin/python

from test import *

def main():
    animals = []
    animals.append(Crow("Brown"))
    animals.append(Cat("John"))
    animals.append(Dog("Alice"))
    for a in animals:
        a.speek()

if __name__ == '__main__':
    main()