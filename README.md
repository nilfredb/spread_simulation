# Spread Simulator

A simple infection spread simulator built with Python and NumPy.

This project models how an infection propagates across a 2D matrix using deterministic and probabilistic neighborhood rules.

Based on cellular automata concepts and neighborhood propagation systems.

---

## 🧠 Concept

Each position inside the matrix represents a person.

Possible states:

- `0` → Healthy
- `1` → Infected
- `2` → Unknown (reserved for future use)

The simulator evaluates neighboring cells and applies infection rules to simulate spread behavior.

---

## ⚙️ Features

- Custom matrix generation
- Random infected agent spawning
- Manual infection injection
- Neighbor detection system
- Deterministic propagation model
- Probabilistic propagation model
- Healthy/Infected population counting
- Interactive terminal menu

---

## 📦 Requirements

Install dependencies:

```bash
pip install numpy
```

---

## ▶️ Running the Project

Run the simulator:

```bash
python main.py
```

---

## 📊 Simulation Models

### 1. Deterministic Propagation

If an infected person has neighbors, all surrounding neighbors become infected.

This uses Moore Neighborhood logic (8-directional adjacency).

---

### 2. Probabilistic Propagation

Each neighboring cell has a configurable probability of becoming infected.

Example:

```python
probabilidad = 0.35
```

This means each neighbor has a 35% chance of infection.

---

## 🧱 Project Structure

```bash
spread-simulator/
│
├── main.py
├── README.md
└── requirements.txt
```

---

## 🔬 Core Functions

### Infect a Person

```python
infectar_persona(matrix, x, y)
```

---

### Infect Random Person

```python
infectar_aleatorio(matrix)
```

---

### Get Neighbors

```python
obtener_vecinos(matrix, x, y)
```

Returns surrounding coordinates.

---

### Deterministic Spread

```python
simulacion_propagacion(matrix)
```

---

### Probabilistic Spread

```python
simulacion_propagacion_probabilistica(matrix, probabilidad)
```

---

## 🖥 Example Menu

```text
0-) Generar matriz custom
1-) Infectar persona
2-) Ver total de enfermos y sanos
3-) Simular propagacion
4-) Salir
```

---

## 📈 Future Improvements

- Infection recovery mechanics
- Mortality system
- Vaccination simulation
- Heatmap visualization
- GUI interface
- Graph statistics
- Multiple infection types
- Agent behavior system
- Time-based simulation engine

---

## 🛠 Technologies

- Python
- NumPy

---

## 📚 Inspiration

This project is inspired by:

- Cellular automata
- Epidemic simulations
- Conway-style propagation systems
- Mathematical spread models

---

## 👨‍💻 Author

Developed by Nilfred Israel Báez del Rosario.

