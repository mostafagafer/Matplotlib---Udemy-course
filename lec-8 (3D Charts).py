from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt

fig = plt.figure()
chart = fig.add_subplot(1, 1, 1, projection="3d")
X, Y, Z = [1, 2, 3, 4, 5, 6, 7, 8], [2, 5, 3, 8, 9, 5, 6, 1], [3, 6, 2, 7, 5, 4, 5, 6]


chart.plot(X, Y, Z)
chart.set_xlabel("x axis")
chart.set_ylabel("y axis")
chart.set_zlabel("z axis")

plt.show()
