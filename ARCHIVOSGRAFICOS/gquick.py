import matplotlib.pyplot as plt

# Datos de tiempos en segundos
n_elements = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
              20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (en segundos) para cada implementación
python_times = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.003000974655151367, 
                0.003113985061645508, 0.003943920135498047, 0.003999948501586914, 
                0.00400090217590332, 0.007065534591674805, 0.007995843887329102, 
                0.008004426956176758, 0.019999980926513672, 0.03158760070800781, 
                0.03199410438537598, 0.03291440010070801, 0.03310799598693848, 
                0.03875160217285156, 0.0440974235534668]

java_times = [0.000100, 0.000280, 0.000468, 0.000513, 0.000560, 0.000574, 
              0.000707, 0.000726, 0.000769, 0.000809, 0.000927, 0.002563, 
              0.003177, 0.003397, 0.004024, 0.004053, 0.004791, 0.005466, 
              0.006576, 0.006659, 0.009995]

cpp_times = [0, 0, 0, 0, 0, 0.001004, 0, 0.000956, 
              0.000999, 0.001005, 0.00098, 0.001005, 
              0.002003, 0.005005, 0.004996, 0.007077, 
              0.010001, 0.011003, 0.014005, 0.017007, 
              0.019896]

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(n_elements[:len(python_times)], python_times, marker='o', label='Python')
plt.plot(n_elements[:len(java_times)], java_times, marker='o', label='Java')
plt.plot(n_elements[:len(cpp_times)], cpp_times, marker='o', label='C++')

# Configuración del gráfico
plt.title('Comparación de Complejidad Temporal del Quick Sort')
plt.xlabel('Número de Elementos')
plt.ylabel('Tiempo (segundos)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar el layout para que no se corte nada
plt.show()
