#! /Library/Frameworks/Python.framework/Versions/3.7/bin/python3.7
# -*- coding: utf-8 -*-
# Parent class
class Dragon:

    def __init__(self, name, snuggled,
        sleep, hunger, cloaca,
         fire, energy, maturity):
        self.name = name
        self.snuggled = snuggled
        self.sleep = sleep
        self.hunger = hunger
        self.cloaca = cloaca
        self.fire = fire
        self.energy = energy
        self.maturity = maturity

    # instance attribute
    def time_passes():
        pass
        
    def description(self):
        return """{} is snuggled at level {},
         has {} units of sleep,
         is {} level hungry,
         needs to use the bath room on a scale of {} on a scale of 0 - 5,
         has a fire power of {} on a scale of 0 - 5,
         and has {} energy on a 0 - 5 scale.
        """.format(self.name, self.snuggled, self.sleep,
        self.hunger, self.cloaca,
         self.fire, self.energy, self.maturity)

    def snuggle(self, snuggle):
        pass

# test code
timmy = Dragon('Timmy', 5, 5, 0, 0, 0, 5, 1)

print(timmy.name)
print(timmy.description())
