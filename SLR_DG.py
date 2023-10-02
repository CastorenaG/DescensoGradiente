import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el dataset
data = pd.read_csv("C:\\Salary_dataset.csv")

# Extraer las columnas
years_of_experience = data['YearsExperience']
salary = data['Salary']

# Inicializar valores de m y b aleatoriamente o con valores iniciales razonables
m = np.random.randn()
b = np.random.randn()

# Hiperparámetros del descenso de gradiente
learning_rate = 0.01
num_iterations = 1000

# Función de costo (Error Cuadrático Medio)
def mse_loss(y_true, y_pred):
    return ((y_true - y_pred) ** 2).mean()

# Descenso de gradiente
for iteration in range(num_iterations):
    # Calcular las predicciones
    y_pred = m * years_of_experience + b
    
    # Calcular los gradientes
    gradient_m = -2 * (years_of_experience * (salary - y_pred)).mean()
    gradient_b = -2 * (salary - y_pred).mean()
    
    # Actualizar los parámetros m y b
    m -= learning_rate * gradient_m
    b -= learning_rate * gradient_b
    
    # Calcular y mostrar la pérdida en cada iteración (opcional)
    loss = mse_loss(salary, y_pred)
    print(f"Iteración {iteration+1}: Pérdida = {loss}")

# Crea la línea de regresión final
regression_line = m * years_of_experience + b

print(f"Pendiente (m): {m}")
print(f"Intersección (b): {b}")

# Grafica los datos y la línea de regresión
plt.scatter(years_of_experience, salary, label='Datos de salario')
plt.plot(years_of_experience, regression_line, color='red', label='Línea de regresión')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')
plt.legend()
plt.title('Regresión Lineal de Salario vs Años de Experiencia')
plt.grid(True)
plt.show()
