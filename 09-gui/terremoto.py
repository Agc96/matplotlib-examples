# -*- coding: utf-8 -*-
"""
Interfaz gráfica para el movimiento armónico de un edificio, de forma similar
a un terremoto.
@author: Anthony Gutiérrez
"""

import numpy as np
import tkinter as tk
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from scipy.constants import g as gravedad
from tkinter.messagebox import showerror

# Inicializar la ventana
window = tk.Tk()
window.title("Movimiento de un edificio")
window.state("zoomed")

# Inicializar el cuadro de ingreso de datos
frame = tk.Frame(window)
frame.pack(side=tk.LEFT, padx=10)

# Declarar los valores por defecto para los datos de entrada
base = 0.75 # Semibase del edificio (b = B/2)
altura = 5.71 # Semialtura del edificio (h = H/2)
masa = 164200.0
radio = 5.76
amplitud = 0.06 # Amplitud del desplazamiento (movimiento armónico)
amort = 0.5 # Coeficiente de amortiguamiento del desplazamiento (gamma)
periodo = 0.5 # Periodo del desplazamiento

# Función auxiliar para declarar datos de entrada
def generar_dato(frame, row, text, default):
    variable = tk.DoubleVar(value=default)
    label = tk.Label(frame, text=text)
    label.grid(row=row, column=0, padx=5, pady=5)
    entry = tk.Entry(frame, textvariable=variable, justify="right")
    entry.grid(row=row, column=1, padx=5, pady=5)
    return variable

# Declarar datos de entrada
base_var = generar_dato(frame, 0, "Semi-base (m):", base)
altura_var = generar_dato(frame, 1, "Semi-altura (m):", altura)
masa_var = generar_dato(frame, 2, "Masa (kg):", masa)
radio_var = generar_dato(frame, 3, "Radio (m):", radio)
amplitud_var = generar_dato(frame, 4, "Amplitud (m):", amplitud)
amort_var = generar_dato(frame, 5, "Coef. amortiguamiento:", amort)
periodo_var = generar_dato(frame, 6, "Periodo (s):", periodo)

# Generar gráfico principal
fig = Figure(figsize=(5, 2))

# Generar subgráfico del movimiento del edificio
edificio_ax = fig.add_subplot(211, xlim=(-12, 12), ylim=(0, 12))
edificio = Rectangle((-base, 0), 2*base, 2*altura)
edificio_ax.add_patch(edificio)
edificio_ax.grid(True)

# Generar subgráfico de cociente entre los ángulos
angulos_ax = fig.add_subplot(223, xlim=(0, 20), ylim=(-1, 1))
angulos_ln, = angulos_ax.plot([], [], '-b')
angulos_mov, = angulos_ax.plot([], [], 'ro')
angulos_ax.grid(True)

# Generar subgráfico de desplazamiento del edificio
desplazamiento_ax = fig.add_subplot(224, xlim=(0, 20), ylim=(-0.1, 0.1))
desplazamiento_ln, = desplazamiento_ax.plot([], [], '-b')
desplazamiento_mov, = desplazamiento_ax.plot([], [], 'ro')
desplazamiento_ax.grid(True)

# Agregar gráfico a la ventana
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

# Función auxiliar para calcular la nueva posición del edificio
def calcular_posicion(tiempo):
    """
    Calcula la posición de un movimiento armónico amortiguado con los datos
    del edificio.
    """
    global amplitud, amort, periodo
    # Calcular los datos intermedios
    velang = 2 * np.pi / periodo
    assert amort < velang
    velamort = np.sqrt(velang**2 - amort**2)
    # Aplicar la fórmula
    return amplitud * np.exp(-amort * tiempo) * np.cos(velamort * tiempo)

# Función auxiliar para calcular la aceleración del edificio
def calcular_aceleracion(tiempo):
    """
    Calcula la segunda derivada de la posición (es decir, la aceleración) de
    un movimiento armónico amortiguado con los datos del edificio.
    """
    global amplitud, amort, periodo
    # Calcular los datos intermedios
    velang = 2 * np.pi / periodo
    assert amort < velang
    velamort = np.sqrt(velang**2 - amort**2)
    # Aplicar la fórmula
    parte1 = (amort**2 - velamort**2) * np.cos(velamort * tiempo)
    parte2 = (2 * amort * velamort) * np.sin(velamort * tiempo)
    return amplitud * np.exp(-amort * tiempo) * (parte1 + parte2)

def calcular_angulo(tiempo, angulo, velang):
    """
    Calcula el ángulo que tendrá el edificio sometido a un movimiento armónico
    amortiguado.
    """
    global amplitud, amort, periodo, radio, paso
    # Calcular los datos intermedios
    frec = np.sqrt((3*gravedad) / (4*radio))
    frecdelta = frec * paso
    senh = np.sinh(frec * paso)
    cosh = np.cosh(frec * paso)
    acel_ahora = calcular_aceleracion(tiempo)
    acel_despues = calcular_aceleracion(tiempo + paso)
    # Aplicar la fórmula
    parte1 = (senh/frec) * velang
    parte2 = cosh * angulo
    parte3 = ((1 - senh/frecdelta) / gravedad) * acel_despues
    parte4 = ((senh/frecdelta - cosh) / gravedad) * acel_ahora
    parte5 = 0
    return parte1 + parte2 + parte3 + parte4 + parte5

def calcular_velang(tiempo, angulo, velang):
    """
    Calcula la primera derivada del ángulo (velocidad angular) que tendrá el
    edificio sometido a un movimiento armónico amortiguado.
    """
    global amplitud, amort, periodo, radio, paso
    # Calcular los datos intermedios
    frec = np.sqrt((3*gravedad) / (4*radio))
    frecdelta = frec * paso
    senh = np.sinh(frec * paso)
    cosh = np.cosh(frec * paso)
    acel_ahora = calcular_aceleracion(tiempo)
    acel_despues = calcular_aceleracion(tiempo + paso)
    # Aplicar la fórmula
    parte1 = 0 * velang
    parte2 = 0 * angulo
    parte3 = 0 * acel_despues
    parte4 = 0 * acel_ahora
    parte5 = 0
    return parte1 + parte2 + parte3 + parte4 + parte5

def start():
    """
    Calcula los datos para la simulación del movimiento sísmico e inicia una
    animación para observar el movimiento del edificio.
    """
    global base, altura, masa, radio, amplitud, amort, periodo
    global tiempos, posiciones, angulos, anim, paso
    try:
        # Parar la animación anterior, si es que existe
        if anim:
            anim.event_source.stop()
        # Obtener los datos principales
        base = base_var.get()
        altura = altura_var.get()
        masa = masa_var.get()
        radio = radio_var.get()
        amplitud = amplitud_var.get()
        amort = amort_var.get()
        periodo = periodo_var.get()
        # Verificar que los datos sean correctos
        assert (base > 0 and altura > 0 and masa > 0 and radio > 0 and
                amplitud > 0 and amort > 0 and periodo > 0)
        # Inicializar los datos
        alfa = np.arctan(base/altura)
        angulo = 0
        velang = 0
        # Calcular el desplazamiento del edificio
        tiempos, paso = np.linspace(0, 20, 1001, retstep=True)
        posiciones = []
        angulos = []
        for tiempo in tiempos:
            tiempo_real = 10 - tiempo if tiempo <= 10 else tiempo - 10
            # Calcular nuevo desplazamiento
            posicion = calcular_posicion(tiempo_real)
            posiciones.append(posicion)
            # Calcular nueva diferencia entre ángulos
            angulo, velang = (calcular_angulo(tiempo_real, angulo, velang),
                              calcular_velang(tiempo_real, angulo, velang))
            print(angulo, velang)
            angulos.append(0 / alfa)
        # Actualizar valores en los gráficos
        desplazamiento_ln.set_data(tiempos, posiciones)
        angulos_ln.set_data(tiempos, angulos)
        canvas.draw()
        # Iniciar la animación
        anim = FuncAnimation(fig, update, 1000, interval=20, blit=True)
    except Exception as ex:
        print(ex)
        showerror("Error", "No se pudo generar la simulación. Verifique que "
                           "los datos ingresados sean correctos y coherentes.")

def update(index):
    """
    Controla la posición y ángulo del edificio en la simulación del movimiento
    sísmico.
    """
    global tiempos, posiciones, angulos
    # Obtener los datos
    tiempo = tiempos[index]
    posicion = posiciones[index]
    angulo = angulos[index]
    # Actualizar valores en el edificio
    edificio.set_x(posicion - base)
    # TODO: Mover ángulo
    # Actualizar puntos en las líneas
    angulos_mov.set_data(tiempo, angulo)
    desplazamiento_mov.set_data(tiempo, posicion)
    return edificio, desplazamiento_mov, angulos_mov

# Inicializar botones
button = tk.Button(frame, text="Iniciar", command=start)
button.grid(row=7, columnspan=2, padx=5, pady=5)

# Inicializar los valores
anim = None
tiempos = []
posiciones = []
angulos = []
start()
# Interactuar con la ventana
window.mainloop()
