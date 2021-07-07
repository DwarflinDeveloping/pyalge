import random
alges = ["Alge 2", "Alge 3", "Alge 4", "Alge 5", "Alge 6"]
megaalges = ["Grün", "Rot", "Blau", "Gelb"]
colours = ["Grün", "Rot"]


# Generates a random Alge from the lists above
def generate_alge():
    alge = random.choice(alges)
    return alge


# Generates a random Megaalge colour from the lists above
def generate_megaalge():
    colour = random.choice(megaalges)
    return colour


# Generates a random colour from the normal Alge game
def generate_colour():
    colour = random.choice(colours)
    return colour
