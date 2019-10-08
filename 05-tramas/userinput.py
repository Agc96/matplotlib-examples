# -*- coding: utf-8 -*-

"""
Permite el ingreso y visualización de puntos en matplotlib. Si el código se ha
ejecutado con anterioridad, permite la opción de usar los puntos declarados
anteriormente.
"""

import os

import numpy as np
import matplotlib.pyplot as plt

def clear_screen():
    """
    Limpia la terminal.
    """
    command = 'cls' if os.name == 'nt' else 'clear'
    try:
        # Limpiar una terminal de IPython
        from IPython import get_ipython
        get_ipython().magic(command)
    except ImportError:
        # Limpiar una terminal de Python clásico
        os.system(command)

def generate_points():
    """
    Permite el ingreso de coordenadas de una serie de puntos (x, y), separadas
    por comas.
    """
    axes = np.array([])
    points = np.array([])
    # Explicación de la función
    print('Ingrese las coordenadas de un punto (x, y), separadas por comas.')
    print('Por ejemplo: 1, 2. Ingrese -1, -1 para salir.')
    # Lectura de datos
    while True:
        result = input('Ingrese un punto: ')
        try:
            x, y = result.split(',') # Separar las coordenadas
            x = float(x)
            y = float(y) # Convertir las coordenadas a punto flotante
            if x == -1 and y == -1:
                break
            else:
                # Agregar coordenadas a los arreglos
                axes = np.append(axes, [x])
                points = np.append(points, [y])
        except ValueError:
            print('El punto ingresado no es válido.')
    # Devolver los datos ingresados
    return axes, points

def ask_for_points():
    """
    Verifica si los puntos existen con anterioridad, en cuyo caso pregunta al
    usuario si desea usar los puntos declarados anteriormente.
    """
    if missing_global('axes') or missing_global('points'):
        return generate_points()
    # Solicitar al usuario si desea generar puntos
    result = input('¿Desea generar nuevos puntos? (S/N): ')
    while True:
        if result.upper() == 'S':
            clear_arrays() # Limpiar todas las variables que sean arreglos
            return generate_points() # Volver a generar los puntos
        elif result.upper() == 'N':
            return axes, points
        else:
            result = input('Ingrese un comando válido: ')

def missing_global(name):
    """
    Determina si la variable existe de forma global.
    """
    return name not in globals()

def clear_arrays():
    """
    Limpia los arreglos de NumPy de la terminal.
    """
    try:
        # Limpiar variables desde una terminal de IPython
        from IPython import get_ipython
        get_ipython().magic('reset -f array')
    except ImportError:
        # Limpiar variables desde una terminal de Python clásico
        for name in dir():
            obj = globals()[name]
            if isinstance(obj, np.array):
                del obj

def plot_points(axes, points):
    """
    Elabora un gráfico con los datos ingresados por el usuario.
    """
    plt.plot(axes, points, '-ro')
    plt.title('Ejemplo de ingreso y visualización de puntos')
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.show()

def main():
    global axes
    global points
    clear_screen()
    axes, points = ask_for_points()
    plot_points(axes, points)

if __name__ == "__main__":
    main()
