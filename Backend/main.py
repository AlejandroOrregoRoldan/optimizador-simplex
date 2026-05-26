import numpy as np
from logic.simplex_revisado import resolver_simplex_revisado
from logic.graficador import generar_grafico

def iniciar_optimizador():
    print("=========================================")
    print(" SISTEMA DE OPTIMIZACIÓN UNIVERSAL")
    print("=========================================\n")
    
    # === EJEMPLO 1: Wyndor Glass (Maximización con <=) ===
    # Puedes cambiar estos valores para probar el ejemplo de Minimización de la Clase 10
    tipo_optimizacion = 'max' # Escribe 'min' si es minimizar
    C = np.array([3, 5])
    A = np.array([
        [1, 0],
        [0, 2],
        [3, 2]
    ])
    # Aquí es donde le dices al programa de qué tipo es cada fila:
    signos = ['<=', '<=', '<='] 
    b = np.array([4, 12, 18], dtype=float)
    
    # 1. Gráfica (solo si hay 2 variables originales)
    if len(C) == 2:
        generar_grafico(A, b, C)
        
    # 2. Resolución matemática
    resolver_simplex_revisado(C, A, b, signos, tipo_optimizacion)

if __name__ == "__main__":
    iniciar_optimizador()