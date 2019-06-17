import matplotlib.pyplot as plt
import math
import numpy as np
import random

from CelestialClass import Celestial
from VectorClass import Vector

class System:
    def __init__(self):
        self.celestials = []
        self.g = 6.673e-11
        self.timestep = 86400  #seconds = 1 day
        self.t_total = 10000 #*timestep = equivalent to 10000 days

    def read_file(self,file):
        filein = open(file, "r")
        self.name_data = []
        self.distance_data = []
        self.mass_data = []
        self.colour_data = []
        self.radius_data = []
    #read in data from file and assign to relevant lists
        for line in filein.readlines():
            li = line.strip()
            if not li.startswith("#"):
                tokens = line.split(";")
                self.name_data.append(tokens[0])
                self.distance_data.append(float(tokens[1]))
                self.mass_data.append(float(tokens[2]))
                self.colour_data.append(tokens[3])
                self.radius_data.append(float(tokens[4]))
        filein.close

    def calc_init_vel(self):
        self.velocity_data = []
        m_sun = max(self.mass_data)
        for i in range(0, len(self.distance_data)):
            if int(self.distance_data[i]) == 0:
                self.velocity_data.append(0)
            else:
                self.velocity_data.append(math.sqrt(self.g*m_sun/self.distance_data[i]))

    def assign_celestials(self):
        self.body_data = []
    #assign data sets to Celestial class        
        for i in range(0, len(self.name_data)):
            body = Celestial(self.name_data[i], Vector(self.distance_data[i],0), self.mass_data[i], Vector(0,self.velocity_data[i]), self.colour_data[i], self.radius_data[i], self.celestials)
            self.body_data.append(body)

    def info(self):
        for i in range(0, len(self.name_data)):
            print("---------------------------------------------")
            print("Celestial Name : " + str(self.body_data[i].name))
            print("Initial Position (m from Sun): " + str(self.body_data[i].position))
            print("Mass (kg): " + str(self.body_data[i].mass))
            print("Initial Velocity (m/s): " + str(self.body_data[i].velocity))
            print("Simulation Colour : " + str(self.body_data[i].colour))
            print("Radius (m): " + str(self.body_data[i].radius))
    
    def calculate_acceleration(self, i):
        acceleration = Vector(0,0)
        target_body = self.celestials[i]
        for j, other_body in enumerate(self.celestials):
            if j != i:
                r = math.sqrt((target_body.position.x - other_body.position.x)**2 + (target_body.position.y - other_body.position.y)**2)
                FoverM = self.g * other_body.mass / r**3
                acceleration.x += FoverM * (other_body.position.x - target_body.position.x)
                acceleration.y += FoverM * (other_body.position.y - target_body.position.y)
        return acceleration

    def calculate_velocity(self):
        for i, target_body in enumerate(celestials):
            target_body.velocity.x += target_body.acceleration.x * self.timestep
            target_body.velocity.y += target_body.acceleration.y * self.timestep
    
    def update_position(self):
        for i, target_body in enumerate(celestials):
            target_body.position.x += target_body.velocity.x * self.timestep
            target_body.position.y += target_body.velocity.y * self.timestep

    def get_data(self):
        for t in range(0,self.t_total):
            for i, body in enumerate(self.celestials):
                body.position_log.append(body.position)
                body.acceleration = calculate_acceleration(i)
            for i, target_body in enumerate(celestials):
                body.calculate_velocity()
            for i, target_body in enumerate(celestials):
                body.update_position()
            if t%100 == 0:
            print("Day " + str(t))


def main():
    solar = System()
    solar.read_file("solarprojectinput.txt")
    solar.calc_init_vel()
    solar.assign_celestials() 
    solar.info()
    solar.get_data()
main()