import numpy as np
from utils.helpers import imprimir_tablero_revisado
from logic.sensibilidad import reporte_sensibilidad

def resolver_simplex_revisado(C, A, b):
    num_restricciones, num_variables = A.shape
    
    # Agregar variables de holgura (Matriz Identidad)
    A_aumentada = np.hstack((A, np.eye(num_restricciones)))
    C_aumentado = np.concatenate((C, np.zeros(num_restricciones)))
    
    # Variables básicas iniciales (las de holgura)
    variables_basicas = list(range(num_variables, num_variables + num_restricciones))
    variables_no_basicas = list(range(num_variables))
    
    # Matriz base inicial B y su inversa B^-1
    B_inv = np.eye(num_restricciones)
    
    iteracion = 0
    while True:
        C_B = C_aumentado[variables_basicas]
        
        # Calcular solución actual: Xb = B^-1 * b
        Xb = np.dot(B_inv, b)
        Z = np.dot(C_B, Xb)
        
        imprimir_tablero_revisado(iteracion, B_inv, Xb, variables_basicas, variables_no_basicas, Z)
        
        # Calcular los costos reducidos: w = C_B * B^-1
        w = np.dot(C_B, B_inv)
        
        # Z_j - C_j = w * A_j - C_j
        costos_reducidos = []
        for j in variables_no_basicas:
            Zj_Cj = np.dot(w, A_aumentada[:, j]) - C_aumentado[j]
            costos_reducidos.append(Zj_Cj)
            
        # Condición de parada: Si todos los (Zj - Cj) >= 0, es la solución óptima (para maximización)
        if min(costos_reducidos) >= 0:
            print("\n>>> ¡SOLUCIÓN ÓPTIMA ALCANZADA! <<<")
            print(f"Z Máximo = {Z}")
            # Llamar al análisis de sensibilidad
            reporte_sensibilidad(B_inv, C_B, A_aumentada, C_aumentado, variables_basicas)
            break
            
        # Variable que entra: el Zj - Cj más negativo
        indice_entra_local = np.argmin(costos_reducidos)
        variable_entra = variables_no_basicas[indice_entra_local]
        
        # Columna pivote: y_k = B^-1 * A_k
        columna_pivote = np.dot(B_inv, A_aumentada[:, variable_entra])
        
        # Prueba del cociente mínimo para la variable que sale
        ratios = []
        for i in range(num_restricciones):
            if columna_pivote[i] > 0:
                ratios.append(Xb[i] / columna_pivote[i])
            else:
                ratios.append(float('inf'))
                
        if min(ratios) == float('inf'):
            print("\n>>> ERROR: Problema No Acotado <<<")
            break
            
        indice_sale = np.argmin(ratios)
        variable_sale = variables_basicas[indice_sale]
        
        print(f"--> Entra: X{variable_entra + 1} | Sale: X{variable_sale + 1}")
        
        # Actualizar variables básicas y no básicas
        variables_basicas[indice_sale] = variable_entra
        variables_no_basicas[indice_entra_local] = variable_sale
        
        # Actualizar B_inv usando operaciones elementales de fila (Matriz E)
        E = np.eye(num_restricciones)
        E[:, indice_sale] = -columna_pivote / columna_pivote[indice_sale]
        E[indice_sale, indice_sale] = 1 / columna_pivote[indice_sale]
        
        B_inv = np.dot(E, B_inv)
        iteracion += 1