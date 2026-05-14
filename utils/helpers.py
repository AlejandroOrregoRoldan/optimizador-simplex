import numpy as np

def imprimir_tablero_revisado(iteracion, B_inv, Xb, variables_basicas, variables_no_basicas, Z):
    """
    Imprime los valores clave de cada iteración del Simplex Revisado.
    """
    print(f"\n" + "="*40)
    print(f" ITERACIÓN {iteracion} ")
    print("="*40)
    print(f"Valor actual de Z: {Z}")
    print(f"Variables en la Base: {variables_basicas}")
    print(f"Solución actual (Xb): \n{Xb}")
    print(f"Matriz Inversa B^-1: \n{B_inv}")
    print("-" * 40)