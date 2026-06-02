import numpy as np
import streamlit as st
from Backend.utils.helpers import imprimir_tablero_revisado
from Backend.logic.sensibilidad import reporte_sensibilidad

def resolver_simplex_revisado(C, A, b, signos, tipo_opt='max'):
    # Guardamos los valores originales intactos para el reporte de sensibilidad
    b_original_backup = b.copy()
    C_original_backup = C.copy()
    
    num_restricciones, num_variables_originales = A.shape
    M = 1e6 

    if tipo_opt == 'min':
        C = -np.array(C)

    A_aumentada = A.copy().astype(float)
    C_aumentado = list(C)
    variables_basicas = []
    variables_no_basicas = list(range(num_variables_originales))
    columna_actual = num_variables_originales

    for i in range(num_restricciones):
        if b[i] < 0: 
            A_aumentada[i] = -A_aumentada[i]
            b[i] = -b[i]
            signos[i] = '>=' if signos[i] == '<=' else ('<=' if signos[i] == '>=' else '=')

        col_identidad = np.zeros((num_restricciones, 1))
        col_identidad[i, 0] = 1

        if signos[i] == '<=':
            A_aumentada = np.hstack((A_aumentada, col_identidad))
            C_aumentado.append(0)
            variables_basicas.append(columna_actual)
            columna_actual += 1

        elif signos[i] == '>=':
            col_exceso = np.zeros((num_restricciones, 1))
            col_exceso[i, 0] = -1
            A_aumentada = np.hstack((A_aumentada, col_exceso))
            C_aumentado.append(0)
            variables_no_basicas.append(columna_actual)
            columna_actual += 1

            A_aumentada = np.hstack((A_aumentada, col_identidad))
            C_aumentado.append(-M) 
            variables_basicas.append(columna_actual)
            columna_actual += 1

        elif signos[i] == '=':
            A_aumentada = np.hstack((A_aumentada, col_identidad))
            C_aumentado.append(-M) 
            variables_basicas.append(columna_actual)
            columna_actual += 1

    C_aumentado = np.array(C_aumentado, dtype=float)
    B_inv = np.eye(num_restricciones)

    iteracion = 0
    while True:
        C_B = C_aumentado[variables_basicas]
        Xb = np.dot(B_inv, b)
        Z = np.dot(C_B, Xb)

        imprimir_tablero_revisado(iteracion, B_inv, Xb, variables_basicas, variables_no_basicas, Z)

        w = np.dot(C_B, B_inv)
        costos_reducidos = []
        for j in variables_no_basicas:
            Zj_Cj = np.dot(w, A_aumentada[:, j]) - C_aumentado[j]
            costos_reducidos.append(Zj_Cj)

        if all(cr >= -1e-7 for cr in costos_reducidos):
            if tipo_opt == 'min':
                Z = -Z 
            st.success(f"🎉 **¡SOLUCIÓN ÓPTIMA ALCANZADA!** \n\n **Z Óptimo = {round(Z, 4)}**")
            
            # Llamamos al reporte de sensibilidad con todos los datos calculados
            reporte_sensibilidad(B_inv, C_B, A_aumentada, C_aumentado, variables_basicas, variables_no_basicas, Xb, b_original_backup, tipo_opt, num_variables_originales, C_original_backup)
            break

        indice_entra_local = np.argmin(costos_reducidos)
        variable_entra = variables_no_basicas[indice_entra_local]
        columna_pivote = np.dot(B_inv, A_aumentada[:, variable_entra])

        ratios = []
        for i in range(num_restricciones):
            if columna_pivote[i] > 1e-7:
                ratios.append(Xb[i] / columna_pivote[i])
            else:
                ratios.append(float('inf'))

        if min(ratios) == float('inf'):
            st.error("🚨 **ERROR:** Problema No Acotado (Tiene infinitas soluciones).")
            break

        indice_sale = np.argmin(ratios)
        variable_sale = variables_basicas[indice_sale]

        st.info(f"🔄 **Entra a la base:** X{variable_entra + 1} | **Sale de la base:** X{variable_sale + 1}")
        st.divider()

        variables_basicas[indice_sale] = variable_entra
        variables_no_basicas[indice_entra_local] = variable_sale

        E = np.eye(num_restricciones)
        E[:, indice_sale] = -columna_pivote / columna_pivote[indice_sale]
        E[indice_sale, indice_sale] = 1 / columna_pivote[indice_sale]

        B_inv = np.dot(E, B_inv)
        iteracion += 1