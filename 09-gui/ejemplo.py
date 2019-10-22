# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 13:51:35 2019

@author: Agutierrez
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from scipy.constants import g as GRAVEDAD
import tkinter as tk
from tkinter.messagebox import showerror

# Inicializar la ventana
ventana = tk.Tk()
ventana.title("Ejemplo de movimiento telúrico")
ventana.geometry("800x600")

# Función auxiliar para generar datos de entrada
def generar_dato_entrada(ventana, titulo, fila):
    variable = tk.DoubleVar()
    # Configurar etiqueta para los datos
    etiqueta = tk.Label(ventana, text=titulo)
    etiqueta.grid(row=fila, column=0, padx=5, pady=5) # place(x=10, y=fila*30 - 20)
    # Configurar entrada para los datos
    entrada = tk.Entry(ventana, textvariable=variable, justify="right")
    entrada.grid(row=fila, column=1, padx=5, pady=5) # place(x=140, y=fila*30 - 20)
    return variable

def generar_dato_intermedio(ventana, titulo, fila):
    variable = tk.Variable()
    # Configurar etiqueta para los datos
    etiqueta = tk.Label(ventana, text=titulo)
    etiqueta.grid(row=fila, column=0, padx=5, pady=5)
    # Configurar entrada para los datos
    entrada = tk.Entry(ventana, textvariable=variable, justify="right",
                       state="disabled")
    entrada.grid(row=fila, column=1, padx=5, pady=5)
    return variable

# Generar datos de entrada
base_var = generar_dato_entrada(ventana, "Base (m):", 0) # Base (b)
altura_var = generar_dato_entrada(ventana, "Altura (m):", 1) # Altura (h)
masa_var = generar_dato_entrada(ventana, "Masa (kg):", 2) # Masa (M)
radio_var = generar_dato_entrada(ventana, "Radio (m):", 3) # Radio (R)
# Generar datos intermedios
alfa_var = generar_dato_intermedio(ventana, "Ángulo alfa:", 4)
inercia_var = generar_dato_intermedio(ventana, "Inercia (kg*m^2):", 5)

# Función para iniciar la simulación del movimiento telúrico
def simulacion():
    try:
        # Obtener los datos
        base = base_var.get()
        altura = altura_var.get()
        masa = masa_var.get()
        radio = radio_var.get()
        # Calcular los datos restantes
        alfa = np.arctan(base/altura)
        alfa_var.set("{:.4f}".format(alfa))
        inercia = (4/3)*masa*(radio**2)
        inercia_var.set("{:.4f}".format(inercia))
        # TODO: CALCULAR LOS ÁNGULOS, POSICIÓN, VELOCIDAD, ETC.
    except:
        # Mostrar mensaje de error
        showerror("Error", "Hubo un error al realizar la simulación. "
                           "Verifique que los datos sean válidos.")

# Botón de iniciar simulación
btn_iniciar = tk.Button(ventana, text="Iniciar", command=simulacion)
btn_iniciar.grid(row=7, columnspan=2) # place(x=120, y=190)

# Interactuar con la ventana
ventana.mainloop()

