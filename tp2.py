import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def ingresar_entero(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except ValueError:
            print("Por favor, ingrese un numero entero valido.")

def mostrar_resultados(resultado, valores):
    print("Resultados:")
    for sistema, distribucion in resultado.items():
        print(f"Sistema: {sistema}, Distribución: {distribucion}")
    print("Valores:")
    for sistema, valores in valores.items():
        print(f"Sistema: {sistema}, valores: {valores}")

def estadisticos(continuas, discretas):
    resultado = {}
    valores_sistema = {}
    clasificacion = ingresar_entero("Ingrese 1 si desea Distribuciones Discretas, sino 2 para continuas: ")
    
    for sistema, muestra in (discretas.items() if clasificacion == 1 else continuas.items()):
        distribuciones = []
        valores = []  
        if clasificacion == 1:
            media = np.mean(muestra)
            varianza = np.var(muestra)
            valores.append("media: " + str(media))
            valores.append("varianza: " + str(varianza))
            tau = np.var(muestra) / np.mean(muestra)
            valores.append("Estimación de Tau: " + str(tau))
            if tau == 1:
                distribuciones.append("Poisson")
            elif tau < 1:
                distribuciones.append("Binomial") 
            elif tau > 1:
                distribuciones.append("Binomial negativa")
               
        else:
            desv_estand = np.std(muestra)
            mediaa = np.mean(muestra)
            coeficiente_variacion = np.std(muestra) / np.mean(muestra)
            simetria = stats.skew(muestra)
            valores.append("Desvío estandar: " + str(desv_estand))
            valores.append("Media: " + str(mediaa))
            valores.append("Coeficiente de Variación: " + str(coeficiente_variacion))
            valores.append("Coeficiente de Simetria: " + str(simetria))
            if simetria == 0.0:
                distribuciones.append("normal")
                distribuciones.append("Triangular")
                """
                    media = np.mean(muestra)
                    desv_estand = np.std(muestra)
                     = stats.norm(media, desv_estand)
                    plt.figure(figsize=(12, 6))
                    x = np.linspace(normal.ppf(0.01), normal.ppf(0.99), 100)
                     = normal.pdf(x)
                    plt.plot(x, fp)
                    plt.title("Distribución Normal, Sistema: " + sistema + ", Su media es " + str(media) + " y el desvío estándar es: " + str(desv_estand))
                    .ylabel('probabilidad')
                    plt.xlabel('valores')
                    plt.show()
                """
            elif coeficiente_variacion < 1:
                distribuciones.append("Gamma, Weibull")
                distribuciones.append("Triangular")
            elif 0.5 < coeficiente_variacion <= 1:
                distribuciones.append("Exponencial")
                distribuciones.append("Triangular")
        resultado[sistema] = distribuciones
        valores_sistema[sistema] = valores
        
    return resultado, valores_sistema
    

continuas = {
    "Restaurante": [10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105], 
    "Tienda_Clientes": [5, 10, 5, 15, 10, 5, 10, 15, 20, 10, 5, 10, 15, 20, 5, 10, 15, 20, 25, 10, 15, 20, 25, 30, 15, 20, 25, 30, 35, 20],
    "Fabrica_Equipos": [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30],
    "Tienda_Online": [2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 6, 7, 8, 9, 10],
    "Consulta_Medica": [30, 40, 50, 60, 70, 35, 45, 55, 65, 75, 40, 50, 60, 70, 80],
    "Componentes": [100, 120, 140, 160, 180, 110, 130, 150, 170, 190, 115, 135, 155, 175, 195, 120, 140, 160, 180, 200],
    "Estacion_Combustible": [5, 10, 15, 20, 25, 0, 10, 15, 20, 25, 30, 35, 20, 25, 30, 35, 40, 25, 30, 35, 40, 45, 50, 35, 40],
    "Aeropuerto": [45, 55, 65, 75, 85, 50, 60, 70, 80, 90, 55, 65, 75, 85, 95, 60, 70, 80, 90, 100]
}

discretas = {
    "Supermercado": [100, 120, 90, 110, 130, 95, 115, 105, 125, 135, 85, 115, 100, 120, 110, 130, 140, 95, 115, 105, 125, 135, 90, 120, 110, 130, 140, 100, 110, 120],
    "Baterias": [12, 18, 24, 30, 36, 15, 21, 27, 33, 39, 20, 25, 30, 35, 40, 22, 28, 34, 40, 45],
}

resultados = estadisticos(continuas, discretas)
mostrar_resultados(resultados[0], resultados[1])
