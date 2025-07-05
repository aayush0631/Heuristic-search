# Heuristic-search
# 🔼 Hill Climbing Algorithms for Block Sorting

This repository contains two Python implementations of the **Hill Climbing algorithm** to solve a simple block arrangement problem using adjacent swaps. The goal is to sort a list of blocks (like `['C', 'A', 'D', 'B']`) into a target order (e.g., `['A', 'B', 'C', 'D']`).

---

## 📂 Contents

- `hill_climbing_basic.py` – Basic Hill Climbing with a simple heuristic (misplaced blocks).
- `hill_climbing_distance.py` – Modified version with a distance-based heuristic and improved structure.
- `README.md` – This file.

---

## 📌 Problem Description

Given:
- A list of blocks in an initial arrangement.
- A goal arrangement of the same blocks.

You are allowed to **swap only adjacent blocks**. The objective is to reach the goal arrangement using **Hill Climbing**, a local search algorithm.

---

## 🧠 Heuristics Used

### 1️⃣ Basic Version (`hill_climbing_basic.py`)
- **Heuristic**: Count how many blocks are out of place compared to the goal.

```python
def heuristic(state, goal):
    return sum(1 for i in range(len(state)) if state[i] != goal[i])
