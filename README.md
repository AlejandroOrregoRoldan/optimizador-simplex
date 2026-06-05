# Solver de Programación Lineal - UdeA 📈

Este proyecto es una aplicación web interactiva desarrollada en Python para resolver problemas de Programación Lineal (PL) utilizando el algoritmo del **Simplex Revisado** y el **Método de la M Grande**. 

## Características Principales
* **Resolución Universal:** Soporta modelos de Maximización y Minimización con cualquier combinación de signos (`<=`, `>=`, `=`).
* **Paso a Paso:** Muestra los tableros matriciales detallados de cada iteración, permitiendo un seguimiento del comportamiento de las variables básicas y no básicas.
* **Método Gráfico:** Visualización dinámica de la región factible, sombreados por restricciones y trazado de la función objetivo para problemas bidimensionales (2 variables).
* **Análisis de Sensibilidad Completo:** Generación de tablas con calidad industrial (estilo Solver) que detallan el Valor Final, los Precios Sombra, y los rangos de optimalidad y factibilidad (Aumento y Disminución Permisible).

## Requisitos de Instalación
Asegúrate de tener Python instalado en tu sistema. Abre tu terminal y ejecuta el siguiente comando para instalar todas las dependencias necesarias:

```bash
pip install streamlit numpy pandas matplotlib
```
## Instrucciones de Uso
Para levantar la interfaz web interactiva en tu navegador, abre la terminal en el directorio raíz del proyecto y ejecuta el siguiente comando:

```bash
python -m streamlit run Frontend/app.py
```