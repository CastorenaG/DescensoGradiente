Claro, aquí tienes un archivo README que describe los dos programas:

## Programa 1: Regresión Lineal con Descenso de Gradiente

Este programa implementa una regresión lineal simple utilizando el descenso de gradiente para optimizar los coeficientes "b" y "m" de la línea de regresión. Utiliza un conjunto de datos que relaciona el salario con los años de experiencia de los empleados.

### Funcionamiento

1. Carga un conjunto de datos que contiene las columnas de "años de experiencia" y "salario".

2. Inicializa los valores de "m" y "b" aleatoriamente.

3. Define hiperparámetros como la tasa de aprendizaje y el número de iteraciones.

4. Implementa una función de costo (Error Cuadrático Medio).

5. Utiliza el descenso de gradiente para actualizar los valores de "m" y "b" y minimizar la función de costo.

6. Calcula y muestra la línea de regresión final.

7. Grafica los datos y la línea de regresión.

## Programa 2: Optimización con Descenso de Gradiente

Este programa utiliza el descenso de gradiente para encontrar el valor óptimo de una función específica. La función se define como "funcion_a_optimizar(x1, x2)" y el programa busca los valores de "x1" y "x2" que minimizan esta función.

### Funcionamiento

1. Define una función a optimizar llamada "funcion_a_optimizar(x1, x2)".

2. Implementa una función "calcular_gradiente" que calcula el gradiente de la función en un punto dado.

3. Implementa el descenso de gradiente para actualizar los valores de "x1" y "x2" y minimizar la función.

4. Muestra los valores optimizados de "x1" y "x2" y el valor óptimo de la función.

5. Grafica la función y el proceso de optimización.

## Requisitos

Asegúrate de tener las siguientes bibliotecas instaladas antes de ejecutar los programas:

- Pandas
- Matplotlib
- NumPy

## Uso

1. Clona o descarga este repositorio en tu máquina local.

2. Ejecuta el programa deseado:
   - `SLR_DG.py` para la regresión lineal con descenso de gradiente.
   - `Optimizacion_DG.py` para la optimización con descenso de gradiente.

3. Sigue las instrucciones en la consola para comprender el funcionamiento de cada programa.

## Contribuciones

Si deseas contribuir a este proyecto, siéntete libre de hacer un fork y enviar una solicitud de extracción. Estamos abiertos a mejoras, correcciones de errores y nuevas características.

