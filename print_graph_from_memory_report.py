import csv
from matplotlib import pyplot as plt 
# Listas para almacenar las columnas
columna1 = []
columna2 = []
columna3 = []

# Ruta del archivo CSV
archivo_csv = 'sam_memory.csv'
print ("antes de abrir el archivo")
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

plt.plot(columna1, columna2)
plt.plot(columna1, columna3)
plt.grid(True)
plt.ylabel ("valore memoria")
plt.title("memoria")
plt.draw()
plt.tight_layout()
plt.show()
