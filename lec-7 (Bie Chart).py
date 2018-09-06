import matplotlib.pyplot as plt

sizes = [50, 23, 15, 7, 5]
labels = ['Android', 'Apple', 'Windows', "BlackBerry", 'Xiaomi']

colors = ['yellow', 'orange', 'cyan', 'Magenta', 'Red']

plt.pie(sizes, colors=colors, startangle=90, labels=labels)
plt.title('Pie Chart')
plt.legend(title='Legend', loc='lower left')
plt.axis('equal')  # Just to make the pie a more circle
plt.show()
