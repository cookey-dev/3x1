import matplotlib.pyplot as plt
import numpy as np

x = 27

path = []

path.append(x)

while x != 1:
	if x % 2 != 0:
		x = 3 * x + 1
	else:
		x = x / 2
	path.append(x)

ypoints = [0]

for point in path:
	ypoints.append(point)

ypoints = np.array(ypoints)
plt.plot(ypoints)
plt.show()

