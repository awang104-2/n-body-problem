import mass as ms
import numpy as np
import matplotlib.pyplot as plt


earth = ms.Planet(10, 10, [10, 5], [10, 10])
mars = ms.Planet(10, 10, [10, 5], [-10, -10])
position = []
for i in range(1000):

    earth.apply_force(np.array([0, -1]), 0.1)
    pos = earth.get_pos()
    position.append(pos)
position = np.array(position)
position = np.transpose(position)

x = position[0]
y = position[1]

plt.plot(x, y)
plt.show()
