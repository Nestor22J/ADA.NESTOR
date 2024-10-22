import matplotlib.pyplot as plt

# Datos de tiempos en segundos
n_elements = [100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 
              20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

# Tiempos de ejecución (en segundos) para cada implementación
python_times = [0.0, 0.00699925422668457, 0.015024423599243164, 0.0643625259399414, 
                0.16077160835266113, 0.26402735710144043, 0.668975830078125, 
                0.8185598850250244, 0.9697105884552002, 1.0579535961151123, 
                1.3311026096343994, 1.5413188934326172, 6.849605083465576, 
                15.39345908164978, 64.1798005104065, 66.09057378768921, 
                79.8560540676117, 105.32306385040283, 169.9148805141449, 
                268.5377035140991, 779.5309364795685]

java_times = [0.000139, 0.000141, 0.002348, 0.004843, 0.004926, 0.008299, 
              0.015067, 0.021006, 0.027872, 0.036887, 0.044364, 0.064946, 
              0.239014, 0.523815, 0.932750, 1.426298, 2.050475, 2.806410, 
              3.678717, 4.651191, 5.779141]

cpp_times = [0.0, 0.0, 0.0, 0.004, 0.007893, 0.015103, 0.022059, 
              0.030889, 0.045511, 0.059833, 0.072564, 0.091022, 
              0.378165, 0.860634, 1.46983, 2.32047, 3.42269, 4.7401, 
              6.20567, 7.83042, 9.63427]

# Graficar
plt.figure(figsize=(12, 6))
plt.plot(n_elements[:len(python_times)], python_times, marker='o', label='Python')
plt.plot(n_elements[:len(java_times)], java_times, marker='o', label='Java')
plt.plot(n_elements[:len(cpp_times)], cpp_times, marker='o', label='C++')

# Configuración del gráfico
plt.title('Comparación de Complejidad Temporal del Insertion Sort')
plt.xlabel('Número de Elementos')
plt.ylabel('Tiempo (segundos)')
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor legibilidad
plt.grid()
plt.legend()
plt.tight_layout()  # Ajustar el layout para que no se corte nada
plt.show()
