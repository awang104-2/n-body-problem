import numpy as np
G = 10  # 6.67430/10**11
DT = 0.001


class Body:

    def __init__(self, mass=0, velocity=[0, 0], position=[0, 0]):
        self.m = mass  # mass in kilograms
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

    # Returns the direction as a unit vector of the Body passed in from the Body calling the method.
    def get_direction(self, body):
        dir_vector = body.pos - self.pos
        unit_dir_vector = dir_vector/np.linalg.norm(dir_vector)
        return unit_dir_vector


def get_gravity(body1, body2):
    m1 = body2.m
    m2 = body1.m
    displacement = body1.pos - body2.pos
    distance = np.linalg.norm(displacement)
    if distance < 50:
        distance = 50
    return G*m1*m2/distance**2


def apply_dynamics(bodies, dt):
    N = len(bodies)
    for i in range(N):
        for j in range(N):
            if j != i:
                force_mag = get_gravity(bodies[i], bodies[j])
                unit_dir = bodies[i].get_direction(bodies[j])
                f_g = -force_mag * unit_dir  # The gravitational force of bodies[i] applied to bodies[j], dir included.
                bodies[j].apply_force(f_g, dt)
                bodies[i].apply_force(-f_g, dt)


