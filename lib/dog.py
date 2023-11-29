#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
        self._name = None

    def get_name(self):
        print("Retrieving name")
        return self._name 

    def set_name(self, new_name):
        self._name = new_name   
        pass                  
    