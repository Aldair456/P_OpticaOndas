import matplotlib.pyplot as plt
import  numpy as np
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

for i in range(1, 10):  # Recorrer los datos desde el índice 1 al 9
    y_frecuencia.append(float(data[i][0]))  # Convertir a float
    x_masa.append(float(data[i][1]))  # Convertir a float

# Imprimir los datos para verificar
print("MOSTRANDO FRECUENCIA")
for i in range(len(y_frecuencia)):
    print(y_frecuencia[i])

print("MOSTRANDO LA MASA")
for i in range(len(x_masa)):
    print(x_masa[i])

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
ax.set_ylabel('Frecuencia')
ax.set_title('Frecuencia de oscilación vs Masa del oscilador armónico')

# Configurar límites de los ejes
ax.set_xlim(min(x_masa)-10, max(x_masa)+10)
ax.set_ylim(min(y_frecuencia)-0.5, max(y_frecuencia)+0.5)

# Configurar leyenda
ax.legend(['Datos'], loc='best')

# Mostrar y guardar el gráfico
plt.tight_layout()
plt.show()
fig.savefig('grafico2.png')


#-----
# Realizar el ajuste de curva
grado_ajuste = 2  # Grado del polinomio de ajuste (puedes ajustarlo según tus necesidades)
ajuste = np.polyfit(x_masa, y_frecuencia, grado_ajuste)
parametros_ajuste = ajuste.tolist()
tipo_ajuste = f"Polinomio de grado {grado_ajuste}"
# Imprimir los parámetros del ajuste y el tipo de ajuste
print("Parámetros del ajuste:", parametros_ajuste)
print("Tipo de ajuste utilizado:", tipo_ajuste)

# Crear el gráfico
fig, ax = plt.subplots(figsize=(8, 6))

# Graficar los datos
ax.plot(x_masa, y_frecuencia, 'o-', color='k', linewidth=2, markersize=8, label='Datos')

# Añadir la curva de ajuste al gráfico
ajuste_x = np.linspace(min(x_masa), max(x_masa), 100)
ajuste_y = np.polyval(ajuste, ajuste_x)
ax.plot(ajuste_x, ajuste_y, '--', color='r', linewidth=2, label='Ajuste')

# Configurar etiquetas y título
ax.set_xlabel('Masa (kg)')
ax.set_ylabel('Frecuencia')
ax.set_title('Frecuencia de oscilación vs Masa del oscilador armónico')

# Configurar límites de los ejes
ax.set_xlim(min(x_masa)-10, max(x_masa)+10)
ax.set_ylim(min(y_frecuencia)-0.5, max(y_frecuencia)+0.5)

# Configurar leyenda
ax.legend(loc='best')

# Mostrar el gráfico
plt.tight_layout()
plt.show()

# Guardar el gráfico en formato png con un nombre descriptivo
nombre_grafico = 'ajuste_pol_grado2.png'
fig.savefig(nombre_grafico)
print("Gráfico guardado como", nombre_grafico)