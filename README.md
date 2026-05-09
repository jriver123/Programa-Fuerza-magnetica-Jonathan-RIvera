# Calculadora de Fuerza Magnética (Electromagnetismo) 🧲

## 📖 Descripción del Programa
Esta aplicación es una herramienta educativa e interactiva diseñada para automatizar la resolución de problemas de fuerza magnética. A diferencia de una calculadora estándar que solo entrega el resultado final, este software pone un fuerte énfasis en la **demostración del procedimiento matemático**. 

El programa toma los vectores tridimensionales de velocidad, campo magnético y posición, y desglosa paso a paso la operación del **producto vectorial (producto cruz)**, mostrando explícitamente el cálculo de las componentes $\hat{i}$, $\hat{j}$ y $\hat{k}$ mediante el método de determinantes. Es una herramienta ideal para verificar cálculos manuales, comprender el álgebra vectorial aplicada a la física y evitar errores comunes con los signos y la notación científica.

## 🚀 Características

- **Modularidad:** El código está dividido en módulos independientes (Lógica, Interfaz y Ejecución) siguiendo buenas prácticas de ingeniería de software.
- **Escenario 1 (Carga en Movimiento):** Cálculo de la Fuerza de Lorentz ($\vec{F} = q(\vec{v} \times \vec{B})$).
- **Escenario 2 (Conductor Rectilíneo):** Cálculo de la fuerza sobre un cable conductor ($\vec{F} = I(\vec{L} \times \vec{B})$).
- **Desglose Procedimental:** Implementación explícita de la fórmula del determinante para el producto cruz en la interfaz.
- **Interfaz Gráfica (GUI):** Interfaz amigable e intuitiva construida nativamente con `tkinter`, incluyendo manejo de texto adaptable (Word Wrap) y barras de desplazamiento.

## 🛠️ Tecnologías Utilizadas

- **Lenguaje:** Python 3.x
- **Librería de Interfaz:** Tkinter (Standard Library)
- **Conceptos Aplicados:** Física Teórica, Álgebra Vectorial y Programación Modular.

## 📂 Estructura del Proyecto

```text
├── main.py              # Punto de entrada de la aplicación.
├── interfaz.py          # Definición de la ventana, pestañas y manejo de eventos.
└── calculos_fisica.py   # Módulo con la lógica matemática y generación de procedimientos.
