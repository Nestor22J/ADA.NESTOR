import matplotlib.pyplot as plt

# Datos de tiempos en segundos
n_elements = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
              20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (en segundos) para cada implementación
python_times = [0.0, 0.013003826141357422, 0.030997753143310547, 0.15173006057739258, 
                0.33681178092956543, 0.5848112106323242, 1.3680531978607178, 1.7411775588989258, 
                2.027474880218506, 2.2435808181762695, 2.83949875831604, 3.34873104095459, 
                14.642810583114624, 32.812511682510376, 58.36367630958557, 140.8325116634369, 
                173.30756974220276, 205.0060510635376, 226.97827553749084, 285.515460729599, 
                366.046591758728]

java_times = [0.000409, 0.000808, 0.006541, 0.010581, 0.014128, 0.025897, 0.038213, 
              0.056563, 0.079685, 0.100500, 0.129899, 0.132644, 0.934284, 2.336690, 
              4.332961, 6.923273, 10.019056, 13.805403, 18.159439, 23.049853, 
              26.222350]

cpp_times = [0.0, 0.00103, 0.005007, 0.018004, 0.042854, 0.072505, 0.113612, 
              0.16776, 0.234983, 0.313951, 0.396084, 0.481257, 2.05318, 4.77188, 
              8.32695, 13.0716, 19.358, 26.8498, 35.0246, 44.7294, 55.6073]

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(n_elements[:len(python_times)], python_times, marker='o', label='Python')
plt.plot(n_elements[:len(java_times)], java_times, marker='o', label='Java')
plt.plot(n_elements[:len(cpp_times)], cpp_times, marker='o', label='C++')

# Configuración del gráfico
plt.title('Bubble Sort Time Complexity Comparison')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar el layout para que no se corte nada
plt.show()

