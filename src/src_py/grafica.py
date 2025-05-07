import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,7,10]

plt.plot(x, y, label = "Linea", color="blue")

plt.title("Mi primer grafico")
plt.xlabel("Eje de la X")
plt.ylabel("Eje de la Y")

plt.legend()

plt.show()