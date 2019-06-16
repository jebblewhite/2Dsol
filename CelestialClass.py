from VectorClass import Vector

class Celestial:
    def __init__(self, name, position, mass, velocity, colour, radius, celestials):
        self.name = name
        self.position = position
        self.mass = mass
        self.acceleration = 0
        self.velocity = velocity
        self.colour = colour
        self.radius = radius
        celestials.append(self)