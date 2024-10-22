import matplotlib.pyplot as plt

# Tiempos de ejecución de los algoritmos en segundos (C++)
algoritmos_cpp = {
    'Bubble Sort': [
        0.000000, 0.001030, 0.005007, 0.018004, 0.042854, 0.072505, 0.113612, 0.167760,
        0.234983, 0.313951, 0.396084, 0.481257, 2.053180, 4.771880, 8.326950, 13.071600,
        19.358000, 26.849800, 35.024600, 44.729400, 55.607300
    ],

    'Counting Sort': [
        0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.000997,
        0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.001031, 0.001005, 0.001078,
        0.001000, 0.000999, 0.001000, 0.002003, 0.001002
    ],

    'Heap Sort': [
        0.000000, 0.000970, 0.000884, 0.001000, 0.001002, 0.001000, 0.001940, 0.001001,
        0.001000, 0.002001, 0.001966, 0.003239, 0.006117, 0.008981, 0.013036, 0.015993,
        0.018019, 0.020993, 0.025532, 0.029094, 0.032111
    ],

    'Insertion Sort': [
        0.000000, 0.000000, 0.000000, 0.004000, 0.007893, 0.015103, 0.022059, 0.030889,
        0.045511, 0.059833, 0.072564, 0.091022, 0.378165, 0.860634, 1.469830, 2.320470,
        3.422690, 4.740100, 6.205670, 7.830420, 9.634270
    ],

    'Merge Sort': [
        0.000000, 0.000000, 0.001127, 0.001000, 0.001001, 0.000998, 0.002003, 0.003043,
        0.001999, 0.002997, 0.004001, 0.004001, 0.008990, 0.011887, 0.014982, 0.021632,
        0.025892, 0.029867, 0.035107, 0.037995, 0.044056
    ],

    'Quick Sort': [
        0.000000, 0.000000, 0.000000, 0.000000, 0.000000, 0.001004, 0.000000, 0.000956,
        0.000999, 0.001005, 0.000980, 0.001005, 0.002003, 0.005005, 0.004996, 0.007077,
        0.010001, 0.011003, 0.014005, 0.017007, 0.019896
    ],

    'Selection Sort': [
        0.000000, 0.000000, 0.001003, 0.005112, 0.011107, 0.019720, 0.030512, 0.048223,
        0.063001, 0.083396, 0.107508, 0.135082, 0.507018, 1.164450, 2.044880, 3.322540,
        4.906470, 6.610450, 8.675820, 11.013600, 13.662700
    ]
}

# Cantidades de elementos
cantidades_cpp = [
    100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000,
    9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000,
    80000, 90000, 100000
]

# Asegurarse de que todas las listas de tiempos tienen 21 elementos
for key in algoritmos_cpp:
    while len(algoritmos_cpp[key]) < len(cantidades_cpp):
        algoritmos_cpp[key].append(algoritmos_cpp[key][-1])  # Duplicar el último valor para igualar longitud

# Crear la gráfica
plt.figure(figsize=(12, 8))

# Graficar cada algoritmo con líneas
for algoritmo, tiempos in algoritmos_cpp.items():
    plt.plot(cantidades_cpp, tiempos, label=algoritmo)

# Configuración de la gráfica
plt.title('Tiempos de Ejecución de Algoritmos de Ordenamiento (C++)', fontsize=16)
plt.xlabel('Número de Elementos', fontsize=14)
plt.ylabel('Tiempo (segundos)', fontsize=14)

# Configurar los ticks del eje x
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
