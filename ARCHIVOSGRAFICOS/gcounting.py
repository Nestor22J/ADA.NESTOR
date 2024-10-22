import matplotlib.pyplot as plt

# Datos de tiempos en segundos
n_elements = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
              20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (en segundos) para cada implementación
python_times = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0009515285491943359, 0.0010013580322265625, 
                0.0010046958923339844, 0.001004934310913086, 0.0010247230529785156, 
                0.0020017623901367188, 0.002006053924560547, 0.008003711700439453, 
                0.00801539421081543, 0.011922359466552734, 0.013616323471069336, 
                0.013994932174682617, 0.01600813865661621, 0.016076087951660156, 
                0.016998291015625]

java_times = [0.000006, 0.000060, 0.000064, 0.000068, 0.000076, 0.000087, 0.000091, 
              0.000097, 0.000103, 0.000228, 0.000325, 0.000445, 0.000520, 0.000580, 
              0.000644, 0.000671, 0.000769, 0.000862, 0.001206, 0.002359, 
              0.010677]

cpp_times = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.000997, 0.0, 0.0, 0.0, 0.0, 
              0.0, 0.001031, 0.001005, 0.001078, 0.001, 0.000999, 0.001, 
              0.002003, 0.001002]

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(n_elements[:len(python_times)], python_times, marker='o', label='Python')
plt.plot(n_elements[:len(java_times)], java_times, marker='o', label='Java')
plt.plot(n_elements[:len(cpp_times)], cpp_times, marker='o', label='C++')

# Configuración del gráfico
plt.title('Counting Sort Time Complexity Comparison')
plt.xlabel('Number of Elements')
plt.ylabel('Time (seconds)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar el layout para que no se corte nada
plt.show()
