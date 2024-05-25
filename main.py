import mass as ms
import numpy as np
from matplotlib import pyplot as plt


def run():
    earth = ms.Planet(10, 10, [0, 0], [0, 0])
    mars = ms.Planet(10, 10, [10.0, 0.0], [0.0, 10.0])

    e_pos = []
    m_pos = []

    dt = 0.001
    for i in range(7000):
        force_mag = ms.get_gravity(earth, mars)
        unit_dir = earth.get_direction(mars)

        f_g = -force_mag*unit_dir
        mars.apply_force(f_g, dt)

        e_pos.append(earth.get_pos())
        m_pos.append(mars.get_pos())

    return m_pos

    e_pos = np.transpose(e_pos)
    m_pos = np.transpose(m_pos)

    earth_x = e_pos[0]
    earth_y = e_pos[1]
    mars_x = m_pos[0]
    mars_y = m_pos[1]

    plt.scatter(earth_x, earth_y)
    plt.plot(mars_x, mars_y)
    plt.show()


run()

