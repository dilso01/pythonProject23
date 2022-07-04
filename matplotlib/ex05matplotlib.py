import numpy as np
import matplotlib.pyplot as plt

# Ex1: grid no eixo x
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([250, 260, 280, 230, 200, 290, 300, 310, 320, 330])
plt.subplot(1, 1, 1)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, color='r')

plt.grid(axis = 'x')


# Ex2: grid no eixo y
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
plt.subplot(1, 1, 1)
plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")
plt.plot(x, y, color='b')

plt.grid(axis = 'y')

plt.show()