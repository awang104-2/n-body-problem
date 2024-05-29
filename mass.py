import numpy as np
G = 10  # 6.67430/10**11


class Planet:

    def __init__(self, mass=0, radius=0, velocity=[0, 0], position=[0, 0]):
        self.m = mass  # mass in kilograms
        self.r = radius  # radius in meters
        self.pos = np.array(position)
        self.v = np.array(velocity)

    def set_position(self, x, y):
        pos = np.array([x, y])

    def move(self, dt):
        self.pos = self.pos + self.v*dt

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
        a = force/self.m
        self.accelerate(a, dt)
        self.move(dt)

    def get_velocity(self):
        return self.v

    def get_direction(self, planet):
        dir_vector = planet.pos - self.pos
        unit_dir_vector = dir_vector/np.linalg.norm(dir_vector)
        return unit_dir_vector


def get_gravity(planet1, planet2):
    m1 = planet2.m
    m2 = planet1.m
    displacement = planet1.pos - planet2.pos
    distance = np.linalg.norm(displacement)
    return G*m1*m2/distance**2


