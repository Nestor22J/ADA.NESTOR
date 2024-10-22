import matplotlib.pyplot as plt

# Tiempos de ejecución de los algoritmos en segundos
algoritmos = {
    'Bubble Sort': [
        0.0, 0.013, 0.031, 0.152, 0.337, 0.585, 1.368, 1.741, 2.027,
        2.244, 2.839, 3.349, 14.643, 32.813, 58.364, 140.833, 173.308,
        205.006, 226.978, 285.515, 366.047
    ],

    'Counting Sort': [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001, 0.001, 0.001, 0.001,
        0.001, 0.002, 0.002, 0.008, 0.008, 0.012, 0.014, 0.014,
        0.016, 0.017, 0.017
    ],

    'Heap Sort': [
        0.0, 0.0, 0.001, 0.001, 0.008, 0.008, 0.018, 0.019, 0.019,
        0.022, 0.022, 0.025, 0.056, 0.088, 0.120, 0.218, 0.225,
        0.247, 0.281, 0.342, 0.342
    ],

    'Insertion Sort': [
        0.0, 0.007, 0.015, 0.064, 0.161, 0.264, 0.669, 0.819, 0.970,
        1.058, 1.331, 1.541, 6.850, 15.393, 64.180, 66.091, 79.856,
        105.323, 169.915, 268.538, 779.531
    ],

    'Merge Sort': [
        0.0, 0.001, 0.001, 0.001, 0.008, 0.008, 0.011, 0.013, 0.013,
        0.015, 0.015, 0.017, 0.040, 0.056, 0.077, 0.115, 0.135,
        0.137, 0.161, 0.211, 0.211
    ],

    'Quick Sort': [
        0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.003, 0.003, 0.004, 0.004,
        0.004, 0.007, 0.008, 0.008, 0.020, 0.032, 0.032, 0.033,
        0.039, 0.044, 0.044
    ],

    'Selection Sort': [
        0.0, 0.006, 0.013, 0.057, 0.129, 0.224, 0.522, 0.661, 0.823,
        0.844, 1.097, 1.259, 5.584, 12.470, 34.680, 48.359, 54.725,
        65.737, 85.887, 99.438, 702.479
    ]
}

# Cantidades de elementos
cantidades = [
    100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000,
    9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000,
    80000, 90000, 100000
]

# Asegurarse de que todas las listas de tiempos tienen 21 elementos
for key in algoritmos:
    while len(algoritmos[key]) < len(cantidades):
        algoritmos[key].append(algoritmos[key][-1])  # Duplicar el último valor para igualar longitud

# Crear la gráfica
plt.figure(figsize=(12, 8))

# Graficar cada algoritmo con líneas
for algoritmo, tiempos in algoritmos.items():
    plt.plot(cantidades, tiempos, label=algoritmo)

# Configuración de la gráfica
plt.title('Tiempos de Ejecución de Algoritmos de Ordenamiento', fontsize=16)
plt.xlabel('Número de Elementos', fontsize=14)
plt.ylabel('Tiempo (segundos)', fontsize=14)

# Configurar los ticks del eje x para que sean los valores especificados
plt.xticks([100, 1000, 5000, 10000] + list(range(20000, 110000, 10000)), rotation=45)

# Añadir líneas verticales para los puntos especificados
for x in [100, 1000, 5000, 10000] + list(range(20000, 110000, 10000)):
    plt.axvline(x=x, color='grey', linestyle='--', linewidth=0.7)

plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', linewidth=0.5)
plt.legend()
plt.tight_layout()

# Mostrar la gráfica
plt.show()
