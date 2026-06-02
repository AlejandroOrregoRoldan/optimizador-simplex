import numpy as np
import pandas as pd
import streamlit as st

def reporte_sensibilidad(B_inv, C_B, A_aumentada, C_aumentado, variables_basicas, variables_no_basicas, Xb, b_original, tipo_opt, num_vars_originales, C_original):
    st.markdown("---")
    st.markdown("### 📊 Reporte de Sensibilidad Completo")
    
    num_restricciones = len(b_original)
    
    # ==========================================
    # 1. TABLA DE RESTRICCIONES (Factibilidad)
    # ==========================================
    precios_sombra = np.dot(C_B, B_inv)
    if tipo_opt == 'min':
        precios_sombra = -precios_sombra # Ajuste de signo para minimización
        
    aumento_b = []
    disminucion_b = []
    
    for i in range(num_restricciones):
        col_B_inv = B_inv[:, i]
        ratios_aum = []
        ratios_dis = []
        
        for j in range(len(Xb)):
            if col_B_inv[j] < -1e-7:
                ratios_aum.append(-Xb[j] / col_B_inv[j])
            elif col_B_inv[j] > 1e-7:
                ratios_dis.append(Xb[j] / col_B_inv[j])
        
        aum = min(ratios_aum) if ratios_aum else float('inf')
        dis = min(ratios_dis) if ratios_dis else float('inf')
        aumento_b.append(aum)
        disminucion_b.append(dis)
        
    df_restricciones = pd.DataFrame({
        "Restricción": [f"Restricción {i+1}" for i in range(num_restricciones)],
        "Lado Der. (b)": b_original,
        "Precio Sombra": np.round(precios_sombra, 4),
        # Se convierte a cadena de texto (str) para evitar conflicto con Streamlit/PyArrow
        "Aumento Permisible": [str(np.round(x, 4)) if x != float('inf') else "1E+30" for x in aumento_b],
        "Disminución Permisible": [str(np.round(x, 4)) if x != float('inf') else "1E+30" for x in disminucion_b]
    })
    
    # ==========================================
    # 2. TABLA DE VARIABLES (Optimalidad)
    # ==========================================
    w = np.dot(C_B, B_inv)
    costos_reducidos = np.dot(w, A_aumentada) - C_aumentado
    
    aumento_c = []
    disminucion_c = []
    
    for j in range(num_vars_originales):
        if j in variables_no_basicas:
            aum = costos_reducidos[j]
            dis = float('inf')
            # Lógica invertida para minimización
            if tipo_opt == 'min': 
                aumento_c.append(dis)
                disminucion_c.append(aum)
            else:
                aumento_c.append(aum)
                disminucion_c.append(dis)
        else:
            fila_base = variables_basicas.index(j)
            fila_Y = np.dot(B_inv[fila_base, :], A_aumentada)
            
            ratios_aum = []
            ratios_dis = []
            for k in variables_no_basicas:
                y_rk = fila_Y[k]
                if y_rk < -1e-7:
                    ratios_aum.append(-costos_reducidos[k] / y_rk)
                elif y_rk > 1e-7:
                    ratios_dis.append(costos_reducidos[k] / y_rk)
                    
            aum = min(ratios_aum) if ratios_aum else float('inf')
            dis = min(ratios_dis) if ratios_dis else float('inf')
            
            if tipo_opt == 'min':
                aumento_c.append(dis)
                disminucion_c.append(aum)
            else:
                aumento_c.append(aum)
                disminucion_c.append(dis)

    df_variables = pd.DataFrame({
        "Variable": [f"X{j+1}" for j in range(num_vars_originales)],
        "Valor Final": [np.round(Xb[variables_basicas.index(j)], 4) if j in variables_basicas else 0.0 for j in range(num_vars_originales)],
        "Coef. Objetivo (C)": C_original,
        # Se convierte a cadena de texto (str) para evitar conflicto con Streamlit/PyArrow
        "Aumento Permisible": [str(np.round(x, 4)) if x != float('inf') else "1E+30" for x in aumento_c],
        "Disminución Permisible": [str(np.round(x, 4)) if x != float('inf') else "1E+30" for x in disminucion_c]
    })

    # Imprimir tablas en Streamlit
    st.markdown("**1. Celdas de Variables (Coeficientes de la Función Objetivo)**")
    st.dataframe(df_variables, hide_index=True, use_container_width=True)
    
    st.markdown("**2. Restricciones (Recursos y Lados Derechos)**")
    st.dataframe(df_restricciones, hide_index=True, use_container_width=True)