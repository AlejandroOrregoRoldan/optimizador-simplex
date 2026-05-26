import numpy as np
import pandas as pd
import streamlit as st

def reporte_sensibilidad(B_inv, C_B, A, C, variables_basicas):
    st.markdown("---")
    st.markdown("### 📊 Análisis de Sensibilidad")
    
    precios_sombra = np.dot(C_B, B_inv)
    
    # Tabla formal de precios sombra
    df_sombra = pd.DataFrame({
        "Restricción": [f"Restricción {i+1}" for i in range(len(precios_sombra))],
        "Precio Sombra": np.round(precios_sombra, 4)
    })
    
    st.table(df_sombra)
    st.info("Nota: El cálculo de los rangos de optimalidad requerirá expandir las inecuaciones C_B * B^-1 * A - C >= 0.")