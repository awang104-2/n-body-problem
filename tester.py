import numpy as np
import matplotlib.pyplot as plt

xy = np.array([0, 10])
r = 10

velxy = np.array([10, 0])
vel = 10

dt = 0.001

a_c = vel**2/r


def get_dir():
    return xy/np.linalg.norm(xy)


pos = [xy]
for i in range(10000):
    velxy = velxy-a_c*get_dir()*dt
    xy = xy+velxy*dt
    print("self", xy)
    pos.append(xy)

pos = np.transpose(pos)
plt.plot(pos[0], pos[1])

circlex = np.linspace(0,10,1000)
circley = np.sqrt(10**2-circlex**2)
# plt.plot(circlex, circley, linestyle='--')
plt.show()
