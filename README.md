# Solver de Programación Lineal - UdeA 📈

Este proyecto es una aplicación web interactiva desarrollada en Python para resolver problemas de Programación Lineal (PL) utilizando el algoritmo del **Simplex Revisado** y el **Método de la M Grande**. 

## Características Principales
* **Resolución Universal:** Soporta problemas de Maximización y Minimización con cualquier combinación de signos (`<=`, `>=`, `=`).
* **Paso a Paso:** Muestra los tableros matriciales detallados de cada iteración.
* **Método Gráfico:** Visualización dinámica de la región factible y la función objetivo para problemas de 2 variables.
* **Análisis de Sensibilidad Práctico:** Tablas directas que muestran los Precios Sombra y los límites absolutos (Mínimo, Valor Actual y Máximo) para restricciones y variables.

## Requisitos de Instalación
Asegúrate de tener Python instalado y ejecuta el siguiente comando para instalar las dependencias necesarias:

```bash
pip install streamlit numpy pandas matplotlib