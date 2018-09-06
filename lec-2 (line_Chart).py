import matplotlib
import matplotlib.pyplot as plt

x = []
y = []

readFile = open("matplotlib.txt")  # note that the file must be on descktop
data = readFile.read().split("\n")
for i in data:
    val = i.split(",")
    x.append(int(val[0]))
    y.append(int(val[1]))

print(data)
print(x)
print(y)
plt.plot(x, y)
