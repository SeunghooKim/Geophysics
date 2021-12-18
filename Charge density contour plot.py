import numpy as np
import matplotlib.pyplot as plt

q = float(-1)
h = float(75)
x = np.arange(-500, 501, 25)
y = np.arange(-500, 501, 25)
tau = np.zeros((41,41))

for i in range(len(x)):
    for j in range(len(y)):
        tau[i][j] = ((1/(2*np.pi)) * (-q * h) / (x[i]**2 + y[j]**2 + h**2) ** (3/2))

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111)
        
plt.contour(x, y, tau, 25, cmap='Spectral')
plt.title("Surface Charge Density for q=-1c, h=75m, interval 25m", fontsize=15)
plt.xlabel("x position (m)", fontsize=10)
plt.ylabel("y position (m)", fontsize=10)
plt.colorbar(label="Surface Charge Density (c/m^2)", orientation="horizontal")
ax.set_aspect('equal', adjustable='box')

plt.savefig('Q5.png', dpi=100)

plt.show()
