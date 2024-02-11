import csv
from matplotlib import pyplot as plt 
# Listas para almacenar las columnas
columna1 = []
columna2 = []
columna3 = []

# Ruta del archivo CSV
archivo_csv = 'sam_memory.csv'
# Lectura del archivo CSV y almacenamiento de las columnas en las listas
with open(archivo_csv, 'r') as archivo:
    lector_csv = csv.reader(archivo)
    print(lector_csv)
    
    # Iterar sobre las filas del archivo
    for fila in lector_csv:
        print(fila)         
         # Añadir elementos a las listas
        columna1.append(fila[0])
        print (columna1)
        columna2.append(fila[3])
        print (columna2)
        columna3.append(fila[4])
        print (columna3)
        #columna2.append(fila[1])
        
        
print ("----------------------------------------------")   
# Imprimir las listas resultantes
print("Columna 1:", columna1)
print("Columna 2:", columna2)
print("Columna 2:", columna3)

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('time (s)', rotation=45)
ax1.set_ylabel('RSZ', color=color,rotation=90)
ax1.plot(columna1, columna2,color=color)
ax1.set_xticklabels(columna1, rotation=90)

ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Memory', color=color, )  # we already handled the x-label with ax1
ax2.plot(columna1, columna3, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
