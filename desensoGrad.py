import numpy as np
import matplotlib.pyplot as plt

#Función a optimizar
def funcion_a_optimizar(x1, x2):
    return 10 - np.exp(-(x1**2 + 3*x2**2))

# Función para calcular el gradiente de la función
def calcular_gradiente(func, x1, x2, epsilon=1e-5):
    grad_x1 = (func(x1 + epsilon, x2) - func(x1, x2)) / epsilon
    grad_x2 = (func(x1, x2 + epsilon) - func(x1, x2)) / epsilon
    return grad_x1, grad_x2

# Implementar el descenso del gradiente para optimizar los valores de x1 y x2
def descenso_gradiente(func, x1_inicial, x2_inicial, learning_rate, num_iteraciones):
    x1_actual, x2_actual = x1_inicial, x2_inicial
    x1_historia, x2_historia = [x1_actual], [x2_actual]

    for i in range(num_iteraciones):
        grad_x1, grad_x2 = calcular_gradiente(func, x1_actual, x2_actual)
        x1_actual -= learning_rate * grad_x1
        x2_actual -= learning_rate * grad_x2
        x1_historia.append(x1_actual)
        x2_historia.append(x2_actual)

    return x1_historia, x2_historia

# Valores iniciales y parámetros de aprendizaje
x1_inicial, x2_inicial = 1.0, 1.0
learning_rate = 0.1
num_iteraciones = 100

# Realizar el descenso del gradiente
x1_historia, x2_historia = descenso_gradiente(funcion_a_optimizar, x1_inicial, x2_inicial, learning_rate, num_iteraciones)

print("Valores optimizados: x1 =", x1_historia[-1], "x2 =", x2_historia[-1])
print("Valor óptimo de la función:", funcion_a_optimizar(x1_historia[-1], x2_historia[-1]))

# Grafica la función y el proceso de optimización
x1 = np.linspace(-2, 2, 400)
x2 = np.linspace(-2, 2, 400)
X1, X2 = np.meshgrid(x1, x2)
Z = 10 - np.exp(-(X1**2 + 3*X2**2))

plt.figure(figsize=(10, 6))
plt.contour(X1, X2, Z, levels=20, cmap='viridis')
plt.scatter(x1_historia, x2_historia, c='r', marker='o', label='Proceso de Optimización')
plt.xlabel('x1')
plt.ylabel('x2')
plt.legend()
plt.title('Optimización de la Función')
plt.colorbar(label='Valor de la Función')
plt.show()


