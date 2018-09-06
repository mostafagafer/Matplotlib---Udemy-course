import matplotlib.pyplot as plt

fig = plt.figure()

rec = fig.patch


rec.set_facecolor("green")


x = [0, 7, 8, 12]
y = [5, 13, 2, 8]
x2 = [0, 4, 7, 12]
y2 = [3, 7, 1, 12]
x3 = [0, 4, 6, 12]
y3 = [13, 5, 8, 2]

graph1 = fig.add_subplot(2, 2, 1, facecolor="black")

graph1.plot(x, y, 'red', linewidth=4.0)


graph1.tick_params(axis='x', color='white')
graph1.tick_params(axis='y', color='white')

graph1.spines["top"].set_color('white')
graph1.spines["bottom"].set_color('white')
graph1.spines["right"].set_color('white')
graph1.spines["left"].set_color('white')

graph1.set_title("Random", color="white")
graph1.set_xlabel("this is x axex", color="white")
graph1.set_ylabel("this is y axex", color="white")

# Adding multible graphs

graph2 = fig.add_subplot(2, 2, 2, facecolor="black")

graph2.plot(x2, y2, 'yellow', linewidth=2.0)


graph2.tick_params(axis='x', color='white')
graph2.tick_params(axis='y', color='white')

graph2.spines["top"].set_color('white')
graph2.spines["bottom"].set_color('white')
graph2.spines["right"].set_color('white')
graph2.spines["left"].set_color('white')

graph2.set_title("Random", color="white")
graph2.set_xlabel("this is x axex", color="white")
graph2.set_ylabel("this is y axex", color="white")


# --> thw 3rd graph takes a third place only
#graph3 = fig.add_subplot(2, 2, 3, facecolor="black")

# this is how to extend the 3rd graph
graph3 = fig.add_subplot(2, 1, 2, facecolor="black")


graph3.plot(x3, y3, 'orange', linewidth=2.0)


graph3.tick_params(axis='x', color='white')
graph3.tick_params(axis='y', color='white')

graph3.spines["top"].set_color('white')
graph3.spines["bottom"].set_color('white')
graph3.spines["right"].set_color('white')
graph3.spines["left"].set_color('white')

graph3.set_title("Random", color="white")
graph3.set_xlabel("this is x axex", color="white")
graph3.set_ylabel("this is y axex", color="white")


plt.show()
