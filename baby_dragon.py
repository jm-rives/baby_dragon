#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
class Dragon:

    maturation_level = 'mature'

    def __init__(self, name, snuggled, sleep, hunger, cloaca, fire, energy):
        self.name = name
        self.snuggled = snuggled
        self.sleep = sleep
        self.hunger = hunger
        self.cloaca = cloaca
        self.fire = fire
        self.energy = energy

    def snuggle(self, snuggle):
        snuggle_meter = 5

class DragonEgg(Dragon):

    maturation_level = 'neonate'

class BabyDragon(Dragon):

    maturation_level = 'child'


class TeenDragon(Dragon):

    maturation_level = 'immature'
