#!/usr/bin/env python3
"""Create a abstract class"""
from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod
    def sound(self):
        pass
"""create a class dog"""
class Dog(Animal):
    def sound(self):
        return "Bark"
"""create a class cat"""
class Cat(Animal):
    def sound(self):
        return "Meow"
