import numpy as np
import math
import random
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from celluloid import Camera
plt.style.use('seaborn-pastel')

fig = plt.figure()
ax = plt.axes(xlim=(-100, 100), ylim=(-100, 100))
line, = ax.plot([], [], lw=3)
ax.set_facecolor("black")
camera = Camera(fig)
    
x = []
y = []
phi = 1.61803399
radius = phi
inv_radius = 1/radius
dot_size = 100

def animate(i):
  angle = i * ((inv_radius*2) * (math.pi))
  x.append((.5*i) * math.cos(angle))
  y.append((.5*i) * math.sin(angle))
  plt.scatter(x, y, s=dot_size, c='green', edgecolor='yellow', linewidth=.8, alpha=1)
  camera.snap()
  if i == 200:    
    animation = camera.animate()
    animation.save('sunflower.gif', writer='imagemagick')

anim1 = FuncAnimation(plt.gcf(), animate, interval=1)
plt.tight_layout()
plt.show()
