import matplotlib.pyplot as plt

# Datos de ejemplo
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

# Crear el gráfico
plt.plot(x, y)

# Obtener los ejes actuales
ax = plt.gca()

# Rotar el eje x a 45 grados
ax.set_xticklabels(ax.get_xticks(), rotation=45)

# Mostrar el gráfico
plt.show()