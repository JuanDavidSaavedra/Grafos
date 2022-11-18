import matplotlib.pyplot as plt
import numpy as np

cx = [1,2,3,4]
cy = [1,4,9,12]
cy1 = [3,2,8,15]
plt.figure(figsize = (8,6))
plt.plot(cx,cy,marker = "o", linestyle = "--", color = "g", linewidth = 2.0, label="Temperatura")
plt.plot(cx,cy1,marker = "D", linestyle = " ", color = "r", linewidth = 3.0, label="Temperatura")
plt.xlabel("Días")
plt.ylabel("Número de Eventos")
plt.yticks([1,9])
plt.legend(loc = "lower right")
plt.title("Gráfica lineal")
plt.savefig("prueba.png")
plt.show()
