# 🤖 Practice 1 - Search Algorithms in Artificial Intelligence

This repository contains the implementation of two fundamental algorithms in the field of Artificial Intelligence: **A\*** and **Minimax**, developed as part of the Artificial Intelligence course in the Bachelor's Degree in Cybersecurity Engineering.

📅 May 2024  
👨‍💻 Authors: Martín Díaz Benito and Juan Carlos Sastre

---

## 📌 Description

The project is divided into two main parts:

### 🔍 A\* Algorithm

- Custom implementation in Python.
- Simulation of a stack-based block problem (A, B, C).
- Use of heuristics to estimate the number of misplaced blocks.
- Search tree visualization using NetworkX.
- State tracking and successor generation.

### ♟️ Minimax Algorithm

- Simulation of a two-player game with pieces A and B on a 5-position linear board.
- Evaluation of terminal states using a heuristic function.
- Recursive generation of the game tree up to depth 6.
- Alternating MAX and MIN turns.
- Decision tree visualization using NetworkX and Matplotlib.

---

## 🛠️ Technologies and Libraries

- Python 3
- NetworkX – for graph representation
- Matplotlib – for search tree visualization

---

## 📂 Code Structure

- `src/astar.py`: Contains the implementation of the A* algorithm, including:
  - `Stack` class: models the stack-based block problem.
  - `a_star_search()`: main function to execute the A* search and visualize the tree.

- `src/minimax.py`: Contains the implementation of the Minimax algorithm, including:
  - `Tablero` class: models the board and piece movements.
  - `generar_arbol()`: recursive function to build the game tree.
  - `evaluarDistancia()`: evaluation function for leaf nodes and value propagation.

---

## 🎯 Achievements

- ✅ Functional implementation of A* and Minimax.
- ✅ Visualization of search and decision trees.
- ✅ Efficient state and movement management.
- ✅ Application of clean coding and software design practices.

---

## 🧠 Conclusion

This project has been a valuable and challenging experience, allowing us to apply theoretical concepts to practical problems. It strengthened our skills in programming, problem-solving, and data structure visualization.

---

## 📁 Files

- `memoriaIA1.pdf`: Report detailing the implementation and explanation of the practice.
- `src/astar.py`: Source code for the A* algorithm.
- `src/minimax.py`: Source code for the Minimax algorithm.
