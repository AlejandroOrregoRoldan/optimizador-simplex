import matplotlib.pyplot as plt
import numpy as np

def generar_grafico(A, b, c):
    """
    Genera el método gráfico. Solo válido si hay exactamente 2 variables de decisión.
    """
    print("\nGenerando gráfica bidimensional...")
    x = np.linspace(0, max(b)*1.2, 400)
    
    plt.figure(figsize=(8, 6))
    
    # Dibujar las restricciones
    for i in range(len(A)):
        if A[i, 1] != 0:
            y = (b[i] - A[i, 0] * x) / A[i, 1]
            plt.plot(x, y, label=f'Restricción {i+1}')
        else:
            plt.axvline(x=b[i]/A[i, 0], label=f'Restricción {i+1}', color='black')
            
    # Configurar el gráfico
    plt.xlim(0, max(b)*1.2)
    plt.ylim(0, max(b)*1.2)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.title('Método Gráfico - Región Factible')
    plt.legend()
    plt.grid(True)
    plt.show()