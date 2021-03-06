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
    def time_passes(self):
        self.snuggled -= 1
        self.sleep -= 1
        self.hunger += 1
        self.cloaca += 1
        self.fire += 0.5
        self.energy -= 0.5
        self.maturity += 0.5

        return("Time has passed.")

    def snuggle(self):
        if self.snuggled < 5:
            self.snuggled += 1
            return ("""
            Your dragon's snuggle meter
            increased by 1 point to {} on a scale of zero to 5.
            """.format(self.snuggled))
        else:
            return("Your dragon's snuggle meter is FULL!.")

    def sleep_dragon(self):
        if self.sleep < 3:
            self.sleep += 1
            return("""Your dragon slept,
             their sleep increased by 1 point.
             Their sleep meter is now {} on
              a scale of zero to 5""".format(self.sleep))
        else:
            return("""Your dragon's sleep meter is {}
            on a scale of zero to 5,
            they're not sleepy and the refused to go to bed.""".format(self.sleep))

    def feed_dragon(self):
        if self.hunger < 2:
            self.energy = 0.5
            self.hunger += 0.25
            return("""
            You let your dragon get too hungry!
            They have almost no energy and
            you'll have to feed him more slowly
            or they'll get sick!
            """)
        elif self.hunger < 4:
            self.hunger += 1
            self.energy = 4
            return(
            """Your dragon was hungry.
            They ate all the food.
            They're hunger level is {}
            on a scale of zero to 5.""".format(self.hunger))
        else:
            return("""Your dragon wasn't hungry,
            and they made a replica castle
            out of the food you gave them.



            Then then they smashed it with a look of glee.
            """)

    def life_stage(self):
        if self.maturity <= 2:
            return("baby")
        elif self.maturity >= 2 and self.maturity <= 4:
            return("(oh gawd) teenage")
        else:
            return("adult")


    def flight(self):
        # dragon has to be at least a teenager to fly
        if self.maturity >= 2:
            # energy good load light
            if self.energy >= 3 and self.cloaca < 3:
                return("Your dragon flies fast!")
            # energy low load light
            elif self.energy >= 2 and self.cloaca < 3:
                return("Your dragon flies slow! Their energies low.")
            # energy good load high
            elif self.energy >= 3 and self.cloaca >= 3:
                return("Your dragon flight is laggy! Their didn't 'go' before take off.")
            # engery low load high
            elif self.energy <=3 and self.cloaca >= 3:
                return("Your dragon flaps it's wings futily. They too heavy and have no energy.")
            else:
                return("""
                Your dragon rolls over on its bakc and feigns sleep.
                They've been hanging out with the local cats far to often this week.
                """)
        else:
            return("""
            Your dragon looks up at you with big puppy eyes and wiggles it's cute
            widdle wings and runs off as fast as it can on four legs.
            The little one zooms back and forth
            with obvious joy flapping their wings furiously.
            They've got some growing to do be they can take flight.
            But they sure are cute at this age.
            """)




    def description(self):
        return """{} is snuggled at level {},
         has {} units of sleep,
         is {} level hungry,
         needs to use the bath room on a scale of {} on a scale of 0 - 5,
         has a fire power of {} on a scale of 0 - 5,
         and has {} energy on a 0 - 5 scale,
         and they are a {} dragon.
        """.format(self.name, self.snuggled, self.sleep,
        self.hunger, self.cloaca,
         self.fire, self.energy, self.life_stage())

# need status prompt for hunger, bathroom, etcself.

# test code
timmy = Dragon('Timmy', 5, 5, 0, 4, 0, 2, 2)
# for i in range(0, 7):
#     timmy.time_passes()
print(timmy.description())
print(timmy.flight())
