import matplotlib.pyplot as plt
import  numpy as np
from tabulate import tabulate  # Importar la biblioteca tabulate
from scipy.optimize import curve_fit
# Exportar de archivo txt
def read_file(nombre_archivo):
    data = []
    try:
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                datos_linea = linea.strip().split(",")
                data.append(datos_linea)
    except FileNotFoundError:
        print("El archivo no se encontró.")
    return data
x_masa = []  # lista de la masa
y_frecuencia = []
data = read_file('Data_oscilador.txt')  # Leer los datos del archivo una vez
headers = ["Masa (kg)", "Frecuencia (Hz)"]
print(tabulate(data, headers=headers, tablefmt="grid"))

for i in range(1, 10):  # Recorrer los datos desde el índice 1 al 9
    y_frecuencia.append(float(data[i][0]))  # Convertir a float
    x_masa.append(float(data[i][1]))  # Convertir a float

# Configurar el estilo del gráfico
plt.style.use('seaborn-darkgrid')

# Configurar el tamaño de fuente
plt.rcParams.update({'font.size': 12})

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Graficar los datos
ax.plot(x_masa, y_frecuencia, 'o-', color='k', linewidth=2, markersize=8)

# Configurar etiquetas y título
ax.set_xlabel('Masa (kg)')
ax.set_ylabel('Frecuencia (Hz)')
ax.set_title('Frecuencia de oscilación vs Masa del oscilador armónico')

# Configurar límites de los ejes
ax.set_xlim(min(x_masa)-0.1, max(x_masa)+0.1)
ax.set_ylim(min(y_frecuencia)-0.1, max(y_frecuencia)+0.1)

# Configurar leyenda
ax.legend(['Datos'], loc='best')
# Mostrar y guardar el gráfico
plt.tight_layout()
plt.show()
fig.savefig('grafico_original.png')
# todo realizando el cambio
def f(m, k):

    return k / (2 * np.pi) * np.sqrt(1 / m)

# Leer los datos del archivo
data = np.genfromtxt('Data_oscilador.txt', delimiter=',', skip_header=1)

# Obtener los valores de masa y frecuencia
x_masa = data[:, 1]
y_frecuencia = data[:, 0]

# Realizar el ajuste de curva
popt, _ = curve_fit(f, x_masa, y_frecuencia)

# Obtener el valor del parámetro k
k = popt[0]

# Generar valores de masa para graficar la función ajustada
x_masa_fit = np.linspace(min(x_masa), max(x_masa), 100)

# Calcular los valores de frecuencia ajustados
y_frecuencia_fit = f(x_masa_fit, k)

# Configurar el estilo del gráfico
plt.style.use('seaborn-darkgrid')

# Configurar el tamaño de fuente
plt.rcParams.update({'font.size': 12})

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
# Graficar los datos
ax.plot(x_masa, y_frecuencia, 'o', color='k', label='Datos')

# Graficar la función ajustada
ax.plot(x_masa_fit, y_frecuencia_fit, '--', color='r', label='Ajuste')

# Configurar etiquetas y título
ax.set_xlabel('Masa (kg)')
ax.set_ylabel('Frecuencia (HZ)')
ax.set_title('Frecuencia de oscilación vs Masa del oscilador armónico')

# Configurar leyenda
ax.legend(loc='best')

# Mostrar el gráfico
plt.tight_layout()
plt.show()
fig.savefig('grafico_conajuste.png')
# Imprimir los parámetros del ajuste
# Imprimir los parámetros del ajuste y el tipo de ajuste utilizado
print("Parámetros del ajuste:")
for i, param in enumerate(popt):
    print(f"Parámetro  K  = {i+1}: {param}")
print("Tipo de ajuste utilizado: funcion racional   ")
