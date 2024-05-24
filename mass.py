import numpy as np
G = 6.67430/10**11


class Planet:

    def __init__(self, mass=0, radius=0, velocity=[float(0), float(0)], x=float(0), y=float(0)):
        self.m = mass # mass in kilograms
        self.r = radius # radius in meters
        self.pos = np.array([x, y])
        self.v = np.array(velocity)

    def set_position(self, x, y):
        pos = np.array([x, y])

    def move(self, dt):
        self.pos[0] = self.pos[0]+self.v[0]*dt
        self.pos[1] = self.pos[1]+self.v[1]*dt

    def get_pos(self):
        return np.copy(self.pos)

    def accelerate(self, acceleration, dt):
        self.v = self.v + acceleration*dt

    def get_gravity(self, planet):
        M = self.m
        m = planet.m
        displacement = planet.pos - self.pos
        distance = np.linalg.norm(displacement)
        return G*M*m/distance**2

    def apply_force(self, force, dt):
        self.move(dt)
        a = force/self.m
        self.accelerate(a, dt)

    def get_velocity(self):
        return self.v


