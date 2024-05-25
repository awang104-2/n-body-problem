"""
Matplotlib Animation Example

Original author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""
# Modified by awang104 into a class for n-body problem simulations.

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


class Animation:

    def __init__(self, pos, interval):
        self.pos = pos
        self.frames = len(pos)
        self.interval = interval
        self.fig = plt.figure()
        self.ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
        self.line, = self.ax.plot([], [], lw=2, marker='o')

    # initialization function: plot the background of each frame
    def init_f(self):
        self.line.set_data([], [])
        return self.line,

    # animation function.  This is called sequentially
    def animate(self, i):
        x = self.pos[i][0]
        y = self.pos[i][1]
        self.line.set_data(x, y)
        return self.line,

    # Runs and shows the animation.
    def run(self):
        anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init_f, frames=self.frames, interval=self.interval, blit=True)
        plt.show()
        return anim
    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html

