import numpy as np
from logic.simplex_revisado import resolver_simplex_revisado
from logic.graficador import generar_grafico

def iniciar_optimizador():
    print("=========================================")
    print(" SISTEMA DE OPTIMIZACIÓN - SIMPLEX REVISADO")
    print("=========================================\n")
    
    # ---------------------------------------------------------
    # EJEMPLO WYNDOR
    # Max Z = 3X1 + 5X2
    # Sujeto a:
    # 1X1 + 0X2 <= 4
    # 0X1 + 2X2 <= 12
    # 3X1 + 2X2 <= 18
    # ---------------------------------------------------------
    
    # 1. Definir los datos matemáticos
    C = np.array([3, 5]) # Función objetivo
    A = np.array([       # Matriz de restricciones
        [1, 0],
        [0, 2],
        [3, 2]
    ])
    b = np.array([4, 12, 18]) # Lados derechos
    
    # 2. Si el problema tiene 2 variables, mostrar el método gráfico
    if len(C) == 2:
        generar_grafico(A, b, C)
        
    # 3. Resolver paso a paso matemáticamente
    resolver_simplex_revisado(C, A, b)

if __name__ == "__main__":
    iniciar_optimizador()