import matplotlib.pyplot as plt

# Datos de tiempos en segundos
n_elements = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
              20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (en segundos) para cada implementación
python_times = [0.0, 0.0, 0.0010006427764892578, 0.0010235309600830078, 
                0.007998228073120117, 0.008018016815185547, 0.01789712905883789, 
                0.01898670196533203, 0.019110441207885742, 0.022001266479492188, 
                0.02204418182373047, 0.025002717971801758, 0.055999040603637695, 
                0.08825349807739258, 0.12048554420471191, 0.21753215789794922, 
                0.22536611557006836, 0.24678373336791992, 0.281268835067749, 
                0.28234314918518066, 0.3424263000488281]

java_times = [0.000069, 0.000099, 0.000249, 0.000268, 0.000371, 0.000505, 
              0.000754, 0.000903, 0.000997, 0.001066, 0.001198, 0.001652, 
              0.003255, 0.005454, 0.006244, 0.007602, 0.008983, 0.010854, 
              0.014799, 0.016582, 0.018493]

cpp_times = [0.0, 0.00097, 0.000884, 0.001, 0.001002, 0.001, 0.00194, 
              0.001001, 0.001, 0.002001, 0.001966, 0.003239, 0.006117, 
              0.008981, 0.013036, 0.015993, 0.018019, 0.020993, 0.025532, 
              0.029094, 0.032111]

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(n_elements[:len(python_times)], python_times, marker='o', label='Python')
plt.plot(n_elements[:len(java_times)], java_times, marker='o', label='Java')
plt.plot(n_elements[:len(cpp_times)], cpp_times, marker='o', label='C++')

# Configuración del gráfico
plt.title('Comparación de Complejidad Temporal del Heap Sort')
plt.xlabel('Número de Elementos')
plt.ylabel('Tiempo (segundos)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar el layout para que no se corte nada
plt.show()
