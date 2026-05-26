import streamlit as st
import numpy as np
import sys
import os

# Conectar la carpeta Frontend con la carpeta Backend
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Backend.logic.simplex_revisado import resolver_simplex_revisado
from Backend.logic.graficador import generar_grafico

st.set_page_config(page_title="Optimizador Simplex - UdeA", layout="wide")

st.title("📈 Solver de Programación Lineal")
st.markdown("**Método Simplex Revisado y M Grande**")

# --- VALORES POR DEFECTO (Ejemplo Wyndor) ---
default_C = [3.0, 5.0]
default_A = [[1.0, 0.0], [0.0, 2.0], [3.0, 2.0]]
default_b = [4.0, 12.0, 18.0]

st.header("1. Configuración del Problema")
col1, col2, col3 = st.columns(3)

with col1:
    tipo_optimizacion = st.selectbox("Objetivo", ["max", "min"])
with col2:
    num_vars = st.number_input("Número de Variables", min_value=2, value=2, step=1)
with col3:
    num_restricciones = st.number_input("Número de Restricciones", min_value=1, value=3, step=1)

st.header("2. Función Objetivo (Z)")
cols_Z = st.columns(num_vars)
C = []
for i in range(num_vars):
    with cols_Z[i]:
        val_def = default_C[i] if i < len(default_C) else 0.0
        coef = st.number_input(f"Coeficiente X{i+1}", value=val_def, step=1.0, key=f"C_{i}")
        C.append(coef)

st.header("3. Restricciones")
A = []
signos = []
b = []

for i in range(num_restricciones):
    st.markdown(f"**Restricción {i+1}**")
    cols_R = st.columns(num_vars + 2)
    fila_A = []
    
    for j in range(num_vars):
        with cols_R[j]:
            val_def_A = default_A[i][j] if (i < len(default_A) and j < len(default_A[i])) else 0.0
            coef_a = st.number_input(f"X{j+1}", value=val_def_A, step=1.0, key=f"a_{i}_{j}")
            fila_A.append(coef_a)
            
    with cols_R[num_vars]:
        signo = st.selectbox("Signo", ["<=", ">=", "="], key=f"sig_{i}")
        signos.append(signo)
        
    with cols_R[num_vars + 1]:
        val_def_b = default_b[i] if i < len(default_b) else 0.0
        val_b = st.number_input("Lado Der. (b)", value=val_def_b, step=1.0, key=f"b_{i}")
        b.append(val_b)
        
    A.append(fila_A)

st.divider()

if st.button("Resolver Problema", type="primary", use_container_width=True):
    C_np = np.array(C)
    A_np = np.array(A)
    b_np = np.array(b)
    
    st.header("Resultados de la Optimización")
    
    # Aquí es donde le dimos la orden de invertir el orden (2 tercios para tableros, 1 tercio para gráfica)
    col_tableros, col_grafica = st.columns([2, 1])
    
    with col_tableros:
        st.subheader("Procedimiento Paso a Paso")
        try:
            resolver_simplex_revisado(C_np, A_np, b_np, signos, tipo_optimizacion)
        except Exception as e:
            st.error(f"ERROR: El problema está mal planteado o no tiene solución. Detalles: {e}")

    with col_grafica:
        if num_vars == 2:
            st.subheader("Método Gráfico")
            fig = generar_grafico(A_np, b_np, C_np)
            st.pyplot(fig, use_container_width=True)