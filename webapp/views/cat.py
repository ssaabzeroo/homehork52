import random

from django.shortcuts import render


class Cat:

    def __init__(self, name, age=None, satiety=None, happiness=None, photo=None):
        self.name = name
        self.age = age if satiety else random.randint(0, 18)
        self.satiety = satiety if satiety else random.randint(20, 80)
        self.happiness = happiness if happiness else random.randint(20, 80)
        self.photo = photo
