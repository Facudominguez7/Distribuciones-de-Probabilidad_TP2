import numpy as np
from scipy import stats

def mostrar_resultados(resultado):
    print("Resultados:")
    for sistema, distribucion in resultado.items():
        print(f"Sistema: {sistema}, Distribución: {distribucion}")

def estadisticos(continuas, discretas):
    resultado = {}
    clasificacion = int(input("Ingrese 1 si desea Distribuciones Discretas, sino 2 para continuas: "))
    
    for sistema, muestra in (discretas.items() if clasificacion == 1 else continuas.items()):
        distribuciones = []  # Inicializar la lista de distribuciones para cada muestra
        
        if clasificacion == 1:
            media_varianza = np.mean(muestra) / np.var(muestra)
            if 0.5 < media_varianza <= 1:
                distribuciones.append("Poisson")
                distribuciones.append("Triangular")
            elif media_varianza < 1:
                distribuciones.append("Binomial") 
                distribuciones.append("Triangular")
            elif media_varianza > 1:
                distribuciones.append("Binomial negativa")
                distribuciones.append("Triangular")
        else:
            coeficiente_variacion = np.std(muestra) / np.mean(muestra)
            asimetria = stats.skew(muestra)
            if asimetria == 0.0:
                distribuciones.append("normal")
                distribuciones.append("Triangular")
                print ("ASIMETRIA", asimetria, sistema)
            elif coeficiente_variacion < 1:
                distribuciones.append("Gamma, Weibull")
                distribuciones.append("Triangular")
            elif 0.5 < coeficiente_variacion <= 1:
                distribuciones.append("Exponencial")
                distribuciones.append("Triangular")
        resultado[sistema] = distribuciones
        
    return resultado
    

continuas = {
    "Restaurante": [10, 15, 20, 25, 30, 35, 40,  45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105], 
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
mostrar_resultados(resultados)
