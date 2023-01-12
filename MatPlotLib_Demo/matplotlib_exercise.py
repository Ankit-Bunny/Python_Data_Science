import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 100)
y = x * 2
z = x ** 2

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, 0.9, 0.9])
ax.plot(x, y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Tile')
plt.tight_layout()
plt.show()

fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.1, .9, .9])
ax2 = fig.add_axes([0.2, 0.5, .2, .2])
ax1.plot(x, y, color='r')
ax2.plot(x, y)
plt.show()

fig = plt.figure()
ax = fig.add_axes([0.1, 0.1, .9, .9])
ax2 = fig.add_axes([0.2, 0.5, .4, .4])
ax.plot(x, z)
ax.set_xlabel('x')
ax.set_ylabel('z')
ax2.plot(x, y)
ax2.set_title('Zoom')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_xlim([20, 22])
ax2.set_xlim([30, 50])
plt.show()

fig, axes = plt.subplots(1, 2, figsize=(12, 2))

axes[0].plot(x, y, color='blue', ls='--')
axes[1].plot(x, z, color='red', lw=3)
plt.show()
