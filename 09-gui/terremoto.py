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
frame.grid(row=0, column=0)

# Función auxiliar para generar datos de entrada
def generar_dato_entrada(frame, text, row):
    variable = tk.DoubleVar()
    # Configurar etiqueta para los datos
    label = tk.Label(frame, text=text)
    label.grid(row=row, column=0, padx=5, pady=5)
    # Configurar entrada para los datos
    entry = tk.Entry(frame, textvariable=variable, justify="right")
    entry.grid(row=row, column=1, padx=5, pady=5)
    return variable

# Inicializar datos de entrada
base_var = generar_dato_entrada(frame, "Base del edificio (m):", 0) # B
altura_var = generar_dato_entrada(frame, "Altura del edificio (m):", 1) # H
masa_var = generar_dato_entrada(frame, "Masa (kg):", 2) # M
amplitud_var = generar_dato_entrada(frame, "Amplitud (m):", 3) # A
elastica_var = generar_dato_entrada(frame, "Constante elástica:", 4) # k
viscosidad_var = generar_dato_entrada(frame, "Coef. de viscosidad:", 5) # b

def movimiento_amortiguado(tiempo, masa, amplitud, elastica, viscosidad):
    """
    Simula un movimiento armónico amortiguado con los datos del edificio.
    """
    constante = viscosidad / (2*masa)
    vel_angular = np.sqrt(elastica/masa - constante**2)
    return amplitud * np.exp(-constante*tiempo) * np.cos(vel_angular*tiempo)

def iniciar_simulacion():
    try:
        # Obtener los datos desde las entradas
        base = base_var.get()
        altura = altura_var.get()
        masa = masa_var.get()
        radio = radio_var.get()
        amplitud = amplitud_var.get()
        elastica = elastica_var.get()
        viscosidad = viscosidad_var.get()
        # Calcular los datos intermedios
        alfa = np.arctan(base/altura)
    except:
        # Mostrar mensaje de error
        showerror("Error", "Hubo un error al realizar la simulación. "
                           "Verifique que los datos sean válidos.")

def detener_simulacion():
    pass

# Inicializar botones
btn_start = tk.Button(frame, text="Iniciar", command=iniciar_simulacion)
btn_start.grid(row=6, column=0)
btn_stop = tk.Button(frame, text="Detener", command=detener_simulacion)
btn_stop.grid(row=6, column=1)

# Generar gráfico principal
fig = Figure(figsize=(5, 2))
fig.gca(xlim=(-100, 100), ylim=(0, 20)).grid(True)
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().grid(row=0, column=1)

# Interactuar con la ventana
window.mainloop()
