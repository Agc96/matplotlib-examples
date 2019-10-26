# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 18:38:21 2019

@author: Agutierrez
"""

# -*- coding: utf-8 -*-
"""
Interfaz gráfica para el movimiento armónico de un edificio, de forma similar
a un terremoto.
"""

import numpy as np
import tkinter as tk
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter.messagebox import showerror

# Inicializar la ventana
window = tk.Tk()
window.title("Movimiento armónico de un edificio")
window.geometry("800x600")

# Inicializar el frame de ingreso de datos
frame = tk.Frame(window)
frame.pack(side=tk.LEFT)

# Declarar los valores por defecto
base = 0.75
altura = 5.71
masa = 164200
radio = 5.76
amplitud = 10
periodo = 2

# Función auxiliar para generar datos de entrada
def generar_dato_entrada(frame, text, index, default=None):
    variable = tk.DoubleVar(value=default)
    # Configurar etiqueta para los datos
    label = tk.Label(frame, text=text)
    label.grid(row=index, column=0, padx=5, pady=5)
    # Configurar entrada para los datos
    entry = tk.Entry(frame, textvariable=variable, justify="right")
    entry.grid(row=index, column=1, padx=5, pady=5)
    return variable

# Inicializar datos de entrada
base_var = generar_dato_entrada(frame, "Semi-base (m):", 0, base)
altura_var = generar_dato_entrada(frame, "Semi-altura (m):", 1, altura)
masa_var = generar_dato_entrada(frame, "Masa (kg):", 2, masa)
radio_var = generar_dato_entrada(frame, "Radio (m):" , 3, radio)
amplitud_var = generar_dato_entrada(frame, "Amplitud (m):", 4, amplitud)
periodo_var = generar_dato_entrada(frame, "Periodo (s):", 5, periodo)

def calcular_posicion(tiempo, masa, amplitud, elastica, viscosidad):
    """
    Simula la posición de un movimiento armónico amortiguado con los datos
    del edificio.
    """
    parte1 = -viscosidad/(2*masa) # Constante decreciente de amplitud
    parte2 = np.sqrt(elastica/masa - parte1**2) # Velocidad angular
    return amplitud * np.exp(parte1*tiempo) * np.cos(parte2*tiempo)

# Generar gráfico principal
principal_fig = Figure(figsize=(5, 2))
principal_ax = principal_fig.gca(xlim=(-100, 100), ylim=(0, 10))
principal_ax.grid(True)
principal_canvas = FigureCanvasTkAgg(principal_fig, master=window)
principal_canvas.draw()
principal_canvas.get_tk_widget().grid(row=0, column=1)

def calcular_aceleracion(tiempo, masa, amplitud, elastica, viscosidad):
    """
    Simula la segunda derivada de la posición (es decir, la aceleración) de
    un movimiento armónico amortiguado con los datos del edificio.
    """
    parte1 = -viscosidad/(2*masa) # Constante decreciente de amplitud
    parte2 = np.sqrt(elastica/masa - parte1**2) # Velocidad angular
    parte3 = (parte1**2 - parte2**2)*np.cos(parte2*tiempo)
    parte4 = (2*parte1*parte2)*np.sin(parte2*tiempo)
    return amplitud * np.exp(parte1*tiempo) * (parte3 - parte4)

def obtener_valor(variable, mensaje_error):
    try:
        return variable.get()
    except Exception as ex:
        raise AssertionError(mensaje_error) from ex

def iniciar_simulacion():
    try:
        base = obtener_valor(base_var, "La semibase no es válida.")
        altura = obtener_valor(altura_var, "La semialtura no es válida.")
        masa = obtener_valor(masa_var, "La masa no es válida.")
        radio = obtener_valor(radio_var, "El radio no es válido.")
        amplitud = obtener_valor(amplitud_var, "La amplitud no es válida.")
        elastica = obtener_valor(elastica_var, "La const. elástica no es válida.")
        viscosidad = obtener_valor(viscosidad_var, "El coef. viscosidad no es válido.")
        # Calcular el ángulo entre la base y la altura
        assert altura != 0, "La altura no puede ser 0."
        alfa = np.arctan(base/altura)
        # Verificar que es un movimiento amortiguado
        msg = ("Los datos para el movimiento amortiguado no son correctos. "
               "Debe cumplirse que b^2 < 4*k*m, donde:\n"
               "- b es el coeficiente de viscosidad\n"
               "- k es la constante elástica\n"
               "- m es la masa del edificio.")
        assert viscosidad**2 < 4*elastica*masa, msg
        # Mostrar los gráficos
        frames = np.linspace(0, 100, 1001)
        posiciones = calcular_posicion(frames, masa, amplitud, elastica,
                                       viscosidad)
        principal_ax.plot(frames, posiciones, '-o')
        print(posiciones)
        
    except Exception as ex:
        showerror("Error", str(ex))

def detener_simulacion():
    pass

# Inicializar botones
btn_start = tk.Button(frame, text="Iniciar", command=iniciar_simulacion)
btn_start.grid(row=7, column=0)
btn_stop = tk.Button(frame, text="Detener", command=detener_simulacion)
btn_stop.grid(row=7, column=1)

"""
# Mostrar los gráficos
frames = np.linspace(0, 100, 1001)
posiciones = calcular_posicion(frames, masa, amplitud, elastica,
                               viscosidad)
principal_ax.plot(frames, posiciones, '-o')
"""

# Interactuar con la ventana
window.mainloop()
