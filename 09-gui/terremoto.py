# -*- coding: utf-8 -*-
"""
Interfaz gráfica para el movimiento armónico de un edificio, de forma similar
a un terremoto.
"""

import numpy as np
import tkinter as tk
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter.messagebox import showerror

# Inicializar la ventana
window = tk.Tk()
window.title("Movimiento de un edificio")
window.state("zoomed")
# Inicializar el frame de ingreso de datos
frame = tk.Frame(window)
frame.pack(side=tk.LEFT, padx=10)

# Declaración de constantes por defecto
base = 0.75
altura = 5.71
masa = 164200
radio = 5.76
amplitud = 0.1
amort = 0.3
periodo = 0.5
tiempo = 20

# Declarar dato de entrada: semi-base del edificio (b)
base_var = tk.DoubleVar(value=base)
tk.Label(frame, text="Semi-base (m):").grid(row=0, column=0, pady=5)
tk.Entry(frame, textvariable=base_var, justify="right").grid(row=0, column=1, pady=5)
# Declarar dato de entrada: semi-altura del edificio (h)
altura_var = tk.DoubleVar(value=altura)
tk.Label(frame, text="Semi-altura (m):").grid(row=1, column=0, pady=5)
tk.Entry(frame, textvariable=altura_var, justify="right").grid(row=1, column=1, pady=5)
# Declarar dato de entrada: masa del edificio (M)
masa_var = tk.DoubleVar(value=masa)
tk.Label(frame, text="Masa (kg):").grid(row=2, column=0, pady=5)
tk.Entry(frame, textvariable=masa_var, justify="right").grid(row=2, column=1, pady=5)
# Declarar dato de entrada: radio del edificio (R)
radio_var = tk.DoubleVar(value=radio)
tk.Label(frame, text="Radio (m):").grid(row=3, column=0, pady=5)
tk.Entry(frame, textvariable=radio_var, justify="right").grid(row=3, column=1, pady=5)
# Declarar dato de entrada: amplitud del desplazamiento sísmico (A)
ampl_var = tk.DoubleVar(value=amplitud)
tk.Label(frame, text="Amplitud (m):").grid(row=4, column=0, pady=5)
tk.Entry(frame, textvariable=ampl_var, justify="right").grid(row=4, column=1, pady=5)
# Declarar dato de entrada: coeficiente de amortiguamiento del despl. (b)
amort_var = tk.DoubleVar(value=amort)
tk.Label(frame, text="Coef. amortiguamiento:").grid(row=5, column=0, pady=5)
tk.Entry(frame, textvariable=amort_var, justify="right").grid(row=5, column=1, pady=5)
# Declarar dato de entrada: periodo del desplazamiento sísmico (T)
periodo_var = tk.DoubleVar(value=periodo)
tk.Label(frame, text="Periodo (s):").grid(row=6, column=0, pady=5)
tk.Entry(frame, textvariable=periodo_var, justify="right").grid(row=6, column=1, pady=5)
# Declarar dato de entrada: periodo del desplazamiento sísmico (T)
tiempo_var = tk.DoubleVar(value=tiempo)
tk.Label(frame, text="Tiempo total (s):").grid(row=7, column=0, pady=5)
tk.Entry(frame, textvariable=tiempo_var, justify="right").grid(row=7, column=1, pady=5)

# Generar gráfico principal
fig = Figure(figsize=(5, 2))
# Generar subgráfico del movimiento del edificio
edificio_ax = fig.add_subplot(211, xlim=(-2*altura-1, 2*altura+1), ylim=(0, 2*altura+1))
edificio = Rectangle((-base, 0), 2*base, 2*altura)
edificio_ax.add_patch(edificio)
edificio_ax.grid(True)
# Generar subgráfico de cociente entre los ángulos
angulos_ax = fig.add_subplot(223, xlim=(0, tiempo), ylim=(-1, 1))
angulos_ln, = angulos_ax.plot([], [], '-b')
angulos_ax.grid(True)
# Generar subgráfico de desplazamiento del edificio
desplazamiento_ax = fig.add_subplot(224, xlim=(0, tiempo), ylim=(-amplitud, amplitud))
desplazamiento_ln, = desplazamiento_ax.plot([], [], '-b')
desplazamiento_ax.grid(True)

# Agregar gráfico a la ventana
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Función auxiliar para calcular la nueva posición del edificio
def calcular_posicion(valor, amplitud, amort, velamort):
    """
    Simula la posición de un movimiento armónico amortiguado con los datos
    del edificio.
    """
    return amplitud * np.exp(-amort * valor) * np.cos(velamort * valor)

# Función auxiliar para calcular la aceleración del edificio
def calcular_aceleracion(valor, amplitud, amort, velamort):
    """
    Simula la segunda derivada de la posición (es decir, la aceleración) de
    un movimiento armónico amortiguado con los datos del edificio.
    """
    parte1 = (amort**2 - velamort**2) * np.cos(velamort * valor)
    parte2 = (2 * amort * velamort) * np.sin(velamort * valor)
    return amplitud * np.exp(-amort * valor) * (parte1 + parte2)

def start():
    """
    Inicia la simulación del movimiento sísmico.
    """
    try:
        # Obtener los datos principales
        base = base_var.get();          assert base > 0
        altura = altura_var.get();      assert altura > 0
        masa = masa_var.get();          assert masa > 0
        radio = radio_var.get();        assert radio > 0
        amplitud = ampl_var.get();      assert amplitud > 0
        amort = amort_var.get();        assert amort > 0
        periodo = periodo_var.get();    assert periodo > 0
        # Calcular los datos intermedios
        alfa = np.arctan(base/altura)
        velang = 2*np.pi/periodo;       assert amort < velang
        velamort = np.sqrt(velang**2 - amort**2)
        # Calcular el desplazamiento del edificio
        frames = np.linspace(0, tiempo, 1001)
        posiciones = []
        for frame in frames:
            valor = tiempo/2 - frame if frame < tiempo/2 else frame - tiempo/2
            posicion = calcular_posicion(valor, amplitud, amort, velamort)
            posiciones.append(posicion)
        # Actualizar valores en los gráficos
        desplazamiento_ln.set_data(frames, posiciones)
        canvas.draw()
    except Exception as ex:
        print(ex)
        showerror("Error", "No se pudo generar la simulación. Verifique que "
                           "los datos ingresados sean correctos y coherentes.")

def stop():
    pass

# Inicializar botones
tk.Button(frame, text="Iniciar", command=start).grid(row=8, column=0, pady=5)
tk.Button(frame, text="Detener", command=stop).grid(row=8, column=1, pady=5)

# Interactuar con la ventana
window.mainloop()
