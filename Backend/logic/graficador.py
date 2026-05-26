import matplotlib.pyplot as plt
import numpy as np

def generar_grafico(A, b, C):
    # Calculamos un límite máximo para la gráfica
    limite = max(b) * 1.2 if max(b) > 0 else 10
    x = np.linspace(0, limite, 400)
    
    # Crear la figura para Streamlit
    fig, ax = plt.subplots(figsize=(8, 6))
    
    for i in range(len(A)):
        if A[i, 1] != 0:
            y = (b[i] - A[i, 0] * x) / A[i, 1]
            ax.plot(x, y, label=f'Restricción {i+1}')
        else:
            if A[i, 0] != 0:
                ax.axvline(x=b[i]/A[i, 0], label=f'Restricción {i+1}', color='black')
            
    ax.set_xlim(0, limite)
    ax.set_ylim(0, limite)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_title('Método Gráfico - Región Factible')
    ax.legend()
    ax.grid(True)
    
    return fig # Retornamos el objeto figura en lugar de hacer plt.show()