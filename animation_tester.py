import animation as an
import numpy as np
import main

pos = np.transpose([np.linspace(0, 2, 1000), np.linspace(-2, 2, 1000)])

test = an.Animation(pos, 0.0001)
test.run()

circular_motion = an.Animation(main.run(),  0.1)
circular_motion.run()


