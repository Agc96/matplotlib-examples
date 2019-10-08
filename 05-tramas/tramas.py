import math
import os

import numpy as np
import matplotlib.pyplot as plt

def limpiar():
    command = 'cls' if os.name == 'nt' else 'clear'
    try:
        from IPython import get_ipython
        get_ipython().magic(command)
    except:
        os.system(command)

def ejemplo_tramas():    
    # np.linspace indica el intervalo y se indica la cantidad de valores a generar
    # Se puede obtener el valor del intervalo que se ha generado con retstep=True
    rango, intervalo = np.linspace(0, 2, 100, endpoint=False, retstep=True)
    # print('Intervalo')
    # print(intervalo)
    # print('Rango')
    # print(rango)
    
    # Generar al lienzo
    plt.plot(rango, rango, label='Lineal')
    plt.plot(rango, rango**2, label='Cuadrático')
    plt.plot(rango, rango**3, label='Cúbico')    
    plt.xlabel('Eje X')
    plt.ylabel('Eje Y')
    plt.title('Ejemplo de tramas de funciones')
    plt.legend()    
    plt.show()

def ejemplo_resorte():
    amplitud = 0.5 # Amplitud de la función senoidal
    constante = 500 # Constante elástica del resorte
    masa = 10 # Masa del objeto
    
    # Generar los rangos
    rango, intervalo = np.linspace(0, 10, 1000, endpoint=False, retstep=True)
    # print('Intervalo')
    # print(intervalo)
    # print('Rango')
    # print(rango)
    
    # Calcular la velocidad angular
    velocidad = math.sqrt(constante/masa)
    print('Velocidad angular')
    print(velocidad)
    
    # Generar los datos de la función senoidal
    datos = []
    for num in rango:
        datos.append(amplitud * math.sin(velocidad*num))
    # print('Datos')
    # print(datos)
    
    # Generar el lienzo
    plt.plot(rango, datos, label='Senoidal')
    plt.title('Ejemplo 2')
    plt.legend()
    plt.show()

def main():
    limpiar()
    ejemplo_tramas()
    ejemplo_resorte()

if __name__ == "__main__":
    main()
