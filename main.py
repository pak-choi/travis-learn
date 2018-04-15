#!/usr/bin/python

from test import *

def main():
    animals = []
    animals.append(Crow("Brown"))
    animals.append(Cat("John"))
    animals.append(Dog("Alice"))
    animals.append(Crow("HAHA"))
    animals.append(Cat("PAPA"))
    animals.append(Dog("LALA"))
    for a in animals:
        a.speek()

if __name__ == '__main__':
    main()