import numpy as np

def reporte_sensibilidad(B_inv, C_B, A, C, variables_basicas):
    """
    Calcula los precios sombra usando la matriz B^-1 de la última iteración.
    """
    print("\n" + "*"*40)
    print(" ANÁLISIS DE SENSIBILIDAD ")
    print("*"*40)
    
    # Los precios sombra se calculan como W = C_B * B^-1
    precios_sombra = np.dot(C_B, B_inv)
    
    print("Precios Sombra (Valor marginal de cada restricción):")
    for i, p in enumerate(precios_sombra):
        print(f"Restricción {i+1}: {round(p, 2)}")
        
    print("\n*Nota: El cálculo de los rangos de optimalidad requerirá expandir las inecuaciones C_B * B^-1 * A - C >= 0.")