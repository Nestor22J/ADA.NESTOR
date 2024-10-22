import matplotlib.pyplot as plt

# Datos de tiempos en segundos
n_elements = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
              20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (en segundos) para cada implementación
python_times = [0.0, 0.005677461624145508, 0.012749433517456055, 0.05672955513000488, 
                0.12854504585266113, 0.22414088249206543, 0.5215773582458496, 
                0.660738468170166, 0.8229625225067139, 0.8440191745758057, 
                1.0973777770996094, 1.2588448524475098, 5.583828449249268, 
                12.46994662284851, 34.679871797561646, 48.35888195037842, 
                54.72498154640198, 65.7369909286499, 85.8866138458252, 
                99.43820428848267, 702.4788110256195]

java_times = [0.000147, 0.000234, 0.004628, 0.007006, 0.007489, 0.009388, 
              0.012706, 0.017973, 0.025414, 0.035285, 0.043048, 0.099865, 
              0.220563, 0.485521, 0.848578, 1.323567, 1.907970, 2.591084, 
              3.404805, 4.290514, 5.348424]

cpp_times = [0, 0, 0.001003, 0.005112, 0.011107, 0.01972, 
              0.030512, 0.048223, 0.063001, 0.083396, 0.107508, 
              0.135082, 0.507018, 1.16445, 2.04488, 3.32254, 
              4.90647, 6.61045, 8.67582, 11.0136, 13.6627]

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(n_elements[:len(python_times)], python_times, marker='o', label='Python')
plt.plot(n_elements[:len(java_times)], java_times, marker='o', label='Java')
plt.plot(n_elements[:len(cpp_times)], cpp_times, marker='o', label='C++')

# Configuración del gráfico
plt.title('Comparación de Complejidad Temporal del Selection Sort')
plt.xlabel('Número de Elementos')
plt.ylabel('Tiempo (segundos)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar el layout para que no se corte nada
plt.show()
