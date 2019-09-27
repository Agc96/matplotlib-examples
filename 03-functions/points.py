# -*- coding: utf-8 -*-
"""
Mostrar la trayectoria de un objeto, definida desde una función, usando matplotlib.
"""

import math

import numpy as np
import matplotlib.pyplot as plt

def poly(x):
    """Define un movimiento polinómico: f(x) = x^3 + 3x^2 + 5."""
    return x**3 + 3*(x**2) + 5

def sine(x):
    """Define un movimiento sinusoidal: f(x) = 255sen(x) + 548."""
    return 255*math.sin(2*x) + 548

def generate_points(X, function, options, label):
    """
    Genera un arreglo de ordenadas (Y) según la función especificada, y dibuja
    los puntos en el lienzo.
    Algunas de las opciones disponibles son las siguientes:
    - 'o' indica que se deben colocar puntos en forma redonda
    - '-' indica que se debe hacer una línea sólida entre los puntos
    - 'b' indica que la línea debe ser de color azul (blue)
    - 'r' indica que la línea debe ser de color rojo (red)
    """
    # Crear arreglo de ordenadas
    Y = []
    for number in X:
        Y.append(function(number))
    # Dibujar puntos con los arreglos
    plt.plot(X, Y, options, label=label)
    return Y

def generate_report(X, Y_poly, Y_sine):
    # Imprimir cabecera
    print("{:10} {:10} {:10}".format("X", "Y1", "Y2"))
    # Imprimir cada punto
    for index, number in enumerate(X):
        print("{:10.2f} {:10.2f} {:10.2f}".format(number, Y_poly[index], Y_sine[index]))

def main():
    # Crear el arreglo de abscisas
    X = np.arange(0, 10, 0.5)
    # Crear y añadir los arreglos de ordenadas
    Y_poly = generate_points(X, poly, "bo-", "Movimiento polinómico")
    Y_sine = generate_points(X, sine, "ro-", "Movimiento sinusoidal")
    # Mostrar lienzo
    plt.legend()
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Posición registrada (m)")
    plt.show()
    # Mostrar reporte
    generate_report(X, Y_poly, Y_sine)

if __name__ == "__main__":
    main()
