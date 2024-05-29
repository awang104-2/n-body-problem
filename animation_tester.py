import animation as an
import numpy as np
import main

pos = np.transpose([np.linspace(0, 2, 1000), np.linspace(-2, 2, 1000)])

# Test animation for circular motion.
circular_motion = an.Animation(main.run_circle(),  0.1)
circular_motion.run()


