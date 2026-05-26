import numpy as np
import pandas as pd
import streamlit as st

def imprimir_tablero_revisado(iteracion, B_inv, Xb, variables_basicas, variables_no_basicas, Z):
    st.markdown(f"### Iteración {iteracion}")
    st.markdown(f"**Valor actual de Z:** `{round(Z, 4)}`")
    
    # Crear tabla para la base y la Solución (Xb)
    df_base = pd.DataFrame({
        "Variables Básicas": [f"X{v+1}" for v in variables_basicas],
        "Solución (Xb)": np.round(Xb, 4)
    })
    
    # Crear tabla para la Matriz Inversa
    columnas_b = [f"Col {i+1}" for i in range(len(B_inv))]
    df_binv = pd.DataFrame(np.round(B_inv, 4), columns=columnas_b)
    
    # Mostrar las tablas en la web
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Variables en la Base:**")
        st.dataframe(df_base, hide_index=True, use_container_width=True)
    with col2:
        st.markdown("**Matriz Inversa $B^{-1}$:**")
        st.dataframe(df_binv, hide_index=True, use_container_width=True)