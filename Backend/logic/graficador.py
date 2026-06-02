import matplotlib.pyplot as plt
import numpy as np

def generar_grafico(A, b, C, signos):
    # Calculamos un límite máximo para la gráfica
    limite = max(b) * 1.2 if max(b) > 0 else 10
    x = np.linspace(0, limite, 400)
    
    fig, ax = plt.subplots(figsize=(5, 4))
    
    # 1. Dibujar las restricciones y sombreados
    for i in range(len(A)):
        if A[i, 1] != 0:
            y = (b[i] - A[i, 0] * x) / A[i, 1]
            ax.plot(x, y, label=f'Restricción {i+1}')
            
            # Sombreado dinámico según el signo
            if signos[i] == '<=':
                ax.fill_between(x, 0, y, where=(y >= 0), alpha=0.15, color='blue')
            elif signos[i] == '>=':
                ax.fill_between(x, y, limite, alpha=0.15, color='blue')
        else:
            # Caso especial: Línea totalmente vertical
            if A[i, 0] != 0:
                x_val = b[i]/A[i, 0]
                ax.axvline(x=x_val, label=f'Restricción {i+1}', color='black')
                
                # Sombreado dinámico para líneas verticales
                if signos[i] == '<=':
                    ax.axvspan(0, x_val, alpha=0.15, color='blue')
                elif signos[i] == '>=':
                    ax.axvspan(x_val, limite, alpha=0.15, color='blue')
                    
    # --- NUEVO: Línea punteada de la Función Objetivo (Z) ---
    # Calculamos un punto medio representativo para trazar la pendiente
    Z_prueba = (limite / 3) * C[0] + (limite / 3) * C[1]
    
    if C[1] != 0:
        y_z = (Z_prueba - C[0] * x) / C[1]
        ax.plot(x, y_z, color='red', linestyle='--', linewidth=2, label='Función Objetivo (Z)')
    elif C[0] != 0: # Caso donde X2 no existe en la función objetivo
        ax.axvline(x=Z_prueba / C[0], color='red', linestyle='--', linewidth=2, label='Función Objetivo (Z)')
            
    # Configuraciones visuales del plano
    ax.set_xlim(0, limite)
    ax.set_ylim(0, limite)
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlabel('X1')
    ax.set_ylabel('X2')
    ax.set_title('Método Gráfico - Región Factible')
    ax.legend()
    ax.grid(True)
    
    return fig