import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 5, 11)
y = x ** 2

fig, axes = plt.subplots(nrows=1, ncols=2)
plt.tight_layout()
# axes.plot(x, y)
axes[0].plot(x, y)
axes[0].set_title('First plot')
axes[1].plot(y, x)
axes[1].set_title('Second plot')
# for current_axes in axes:
#     current_axes.plot(x, y)
plt.tight_layout()
plt.show()
fig.savefig("plot2.png", dpi=200)

fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.plot(x, x ** 2, label="x**2")
ax.plot(x, x ** 3, label="x**3")
ax.legend()
plt.show()
