import animation as an
import numpy as np

pos = np.transpose([np.linspace(0, 2, 1000), np.linspace(-2, 2, 1000)])

anim = an.Animation(pos, 1)
anim.run()
