# 🤖 Práctica 1 - Algoritmos de Búsqueda en Inteligencia Artificial

Este repositorio contiene la implementación de dos algoritmos fundamentales en el campo de la Inteligencia Artificial: **A\*** y **Minimax**, desarrollados como parte de la asignatura de Inteligencia Artificial del Grado en Ingeniería de la Ciberseguridad.

📅 Mayo 2024  
👨‍💻 Autores: Martín Díaz Benito Álvarez y Juan Carlos Sastre García

---

## 📌 Descripción

La práctica se divide en dos partes principales:

### 🔍 Algoritmo A\*

- Implementación desde cero en Python.
- Simulación de un problema de pilas con bloques (A, B, C).
- Uso de heurísticas para calcular el número de bloques desordenados.
- Visualización del árbol de búsqueda con NetworkX.
- Gestión de estados visitados y generación de sucesores.

### ♟️ Algoritmo Minimax

- Simulación de un juego entre dos fichas (A y B) en un tablero lineal de 5 posiciones.
- Evaluación de estados terminales con una función heurística.
- Generación recursiva del árbol de juego hasta profundidad 6.
- Alternancia entre turnos de MAX y MIN.
- Visualización del árbol de decisiones con NetworkX y Matplotlib.

---

## 🛠️ Tecnologías y Librerías

- Python 3
- NetworkX – para la representación de grafos
- Matplotlib – para la visualización del árbol de búsqueda

---

## 📂 Estructura del Código

- `Stack`: clase para representar el estado del problema de las pilas.
- `Tablero`: clase para simular el juego de fichas en el algoritmo Minimax.
- `a_star_search()`: función principal para ejecutar el algoritmo A*.
- `generar_arbol()`: función recursiva para construir el árbol de juego con Minimax.
- `evaluarDistancia()`: función de evaluación para nodos hoja y propagación de valores.

---

## 🎯 Objetivos Alcanzados

- ✅ Implementación funcional de A* y Minimax.
- ✅ Visualización de árboles de búsqueda.
- ✅ Gestión eficiente de estados y movimientos.
- ✅ Aplicación de buenas prácticas de programación.

---

## 🧠 Conclusión

Este proyecto ha sido una experiencia enriquecedora que ha permitido aplicar conceptos teóricos a problemas prácticos, reforzando habilidades en programación, resolución de problemas y visualización de estructuras de datos.

---

## 📁 Archivos

- `memoriaIA1.pdf`: Documento explicativo de la práctica y el código desarrollado.
- `main.py`: Código fuente


