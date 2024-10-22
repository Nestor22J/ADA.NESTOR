import matplotlib.pyplot as plt

# Datos de tiempos en segundos
n_elements = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
              20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (en segundos) para cada implementación
python_times = [0.0, 0.0010004043579101562, 0.001001596450805664, 0.0010607242584228516, 
                0.008002519607543945, 0.008077144622802734, 0.01099848747253418, 
                0.012592554092407227, 0.012883901596069336, 0.014998912811279297, 
                0.01503133773803711, 0.017005205154418945, 0.039999961853027344, 
                0.05648016929626465, 0.07739043235778809, 0.11453461647033691, 
                0.1353762149810791, 0.1367356777191162, 0.16074872016906738, 
                0.16079401969909668, 0.21087050437927246]

java_times = [0.000058, 0.000318, 0.000352, 0.000598, 0.000607, 0.000648, 
              0.000753, 0.001003, 0.001103, 0.001262, 0.002172, 0.004090, 
              0.005147, 0.005382, 0.005644, 0.008079, 0.009221, 0.010268, 
              0.011837, 0.015577, 0.015849]

cpp_times = [0.0, 0.0, 0.001127, 0.001, 0.001001, 0.000998, 0.002003, 
              0.003043, 0.001999, 0.002997, 0.004001, 0.004001, 
              0.00899, 0.011887, 0.014982, 0.021632, 0.025892, 
              0.029867, 0.035107, 0.037995, 0.044056]

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(n_elements[:len(python_times)], python_times, marker='o', label='Python')
plt.plot(n_elements[:len(java_times)], java_times, marker='o', label='Java')
plt.plot(n_elements[:len(cpp_times)], cpp_times, marker='o', label='C++')

# Configuración del gráfico
plt.title('Comparación de Complejidad Temporal del Merge Sort')
plt.xlabel('Número de Elementos')
plt.ylabel('Tiempo (segundos)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar el layout para que no se corte nada
plt.show()
