import mass as ms
import numpy as np
import matplotlib.pyplot as plt


earth = ms.Planet(10, 10, [0, 0], [0, 0])
mars = ms.Planet(10, 10, [10.0, 0.0], [0.0, 10.0])

e_pos = []
m_pos = []

dt = 0.001
for i in range(20000):
    force_mag = ms.get_gravity(earth, mars)
    unit_dir = earth.get_direction(mars)

    f_r = -(10**2*10/10)*unit_dir
    mars.apply_force(f_r, dt)

    e_pos.append(earth.get_pos())
    m_pos.append(mars.get_pos())

e_pos = np.transpose(e_pos)
m_pos = np.transpose(m_pos)

earth_x = e_pos[0]
earth_y = e_pos[1]
mars_x = m_pos[0]
mars_y = m_pos[1]

plt.scatter(earth_x, earth_y)
plt.plot(mars_x, mars_y)
plt.show()
