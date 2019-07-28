"""
Prototype
- When it's easier to copy an existing object to fully initialize
  a new one
- A partially or fully initialized object that you copy (clone) and make use of

Motivation
- Complicated objects (e.g., cars) aren't designed from scratch
  - They iterate exists designs
- An existing (partially or fully constructed) design is a Prototype
- We make a copy (clone) the prototype and customize it
  - Requires a 'deep copy' support
- We make the cloning convenient (e.g., via a Factory)
"""

import copy

class Address:
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} lives at {self.address}'

john = Person('John', Address('123 London Road', 'London', 'UK'))
print(john)

# does not work
# jane = john
# jane.name = john

# need to make deep copy
jane = copy.deepcopy(john)
jane.name = 'Jane'
jane.address.street_address = '124 London Road'
print(jane)