import matplotlib.pyplot as plt
import numpy as np


pos = np.arange(6)+0.5  # +.5 desn't effect

names = ['Avi', 'Jose', 'Bob', 'Nick', 'Zelda', 'Matt']
plt.barh(pos, (4, 8, 12, 3, 17, 6), align="center", color="magenta")  # allign center dosen't effect
plt.xlabel("Height in inches", color="Red")
plt.ylabel("Students", color="Red")
plt.title("height of students in inches", color="blue")
plt.tick_params(axis="x", colors="k")
plt.tick_params(axis="y", colors="k")

# how to adjustm but can be change
#plt.subplot_adjust(left=0.11, bottom=0.12, right=.94)

plt.yticks(pos, names)
plt.show()
