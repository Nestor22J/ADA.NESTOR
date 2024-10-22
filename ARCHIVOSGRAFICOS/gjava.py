import matplotlib.pyplot as plt

# Tiempos de ejecución de los algoritmos en segundos (Java)
algoritmos_java = {
    'Bubble Sort': [
        0.000409, 0.000808, 0.006541, 0.010581, 0.014128, 0.025897, 0.038213, 0.056563,
        0.079685, 0.100500, 0.129899, 0.132644, 0.934284, 2.336690, 4.332961, 6.923273,
        10.019056, 13.805403, 18.159439, 23.049853, 26.222350
    ],

    'Merge Sort': [
        0.000058, 0.000318, 0.000352, 0.000598, 0.000607, 0.000648, 0.000753, 0.001003,
        0.001103, 0.001262, 0.002172, 0.004090, 0.005147, 0.005382, 0.005644, 0.008079,
        0.009221, 0.010268, 0.011837, 0.015577, 0.015849
    ],

    'Counting Sort': [
        0.000006, 0.000060, 0.000064, 0.000068, 0.000076, 0.000087, 0.000091, 0.000097,
        0.000103, 0.000228, 0.000325, 0.000445, 0.000520, 0.000580, 0.000644, 0.000671,
        0.000769, 0.000862, 0.001206, 0.002359, 0.010677
    ],

    'Insertion Sort': [
        0.000139, 0.000141, 0.002348, 0.004843, 0.004926, 0.008299, 0.015067, 0.021006,
        0.027872, 0.036887, 0.044364, 0.064946, 0.239014, 0.523815, 0.932750, 1.426298,
        2.050475, 2.806410, 3.678717, 4.651191, 5.779141
    ],

    'Heap Sort': [
        0.000069, 0.000099, 0.000249, 0.000268, 0.000371, 0.000505, 0.000754, 0.000903,
        0.000997, 0.001066, 0.001198, 0.001652, 0.003255, 0.005454, 0.006244, 0.007602,
        0.008983, 0.010854, 0.014799, 0.016582, 0.018493
    ],

    'Quick Sort': [
        0.000100, 0.000280, 0.000468, 0.000513, 0.000560, 0.000574, 0.000707, 0.000726,
        0.000769, 0.000809, 0.000927, 0.002563, 0.003177, 0.003397, 0.004024, 0.004053,
        0.004791, 0.005466, 0.006576, 0.006659, 0.009995
    ],

    'Selection Sort': [
        0.000147, 0.000234, 0.004628, 0.007006, 0.007489, 0.009388, 0.012706, 0.017973,
        0.025414, 0.035285, 0.043048, 0.099865, 0.220563, 0.485521, 0.848578, 1.323567,
        1.907970, 2.591084, 3.404805, 4.290514, 5.348424
    ]
}

# Cantidades de elementos
cantidades_java = [
    100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000,
    9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000,
    80000, 90000, 100000
]

# Asegurarse de que todas las listas de tiempos tienen 21 elementos
for key in algoritmos_java:
    while len(algoritmos_java[key]) < len(cantidades_java):
        algoritmos_java[key].append(algoritmos_java[key][-1])  # Duplicar el último valor para igualar longitud

# Crear la gráfica
plt.figure(figsize=(12, 8))

# Graficar cada algoritmo con líneas
for algoritmo, tiempos in algoritmos_java.items():
    plt.plot(cantidades_java, tiempos, label=algoritmo)

# Configuración de la gráfica
plt.title('Tiempos de Ejecución de Algoritmos de Ordenamiento (Java)', fontsize=16)
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
