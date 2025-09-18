# 🧭 Travelling Salesman Problem (TSP)

The **Travelling Salesman Problem (TSP)** is one of the most famous problems in computer science and operations research.  
It asks:

> Given `n` cities and the distances between each pair, find the shortest possible route that visits each city exactly once and returns to the starting point.

---

## 🔹 Problem Types

1. **Decision Version (NP-Complete)**  
   - Question: *"Does there exist a tour with cost ≤ K?"*
   - Belongs to **NP-Complete** problems.

2. **Optimization Version (NP-Hard)**  
   - Question: *"What is the minimum-cost tour?"*
   - Classified as **NP-Hard**, meaning no known polynomial-time algorithm exists for solving it exactly.

---

## 🔹 Complexity Analysis

### 1. Brute Force
- Try all possible permutations of cities.
- Number of tours: `(n-1)! / 2`  
- **Time Complexity:** `O(n!)`  
- **Accuracy:** ✅ Exact (but impractical for large `n`).

---

### 2. Dynamic Programming (Held–Karp Algorithm)
- Uses bitmasking and DP to reduce redundant calculations.  
- **Time Complexity:** `O(n² * 2^n)`  
- **Space Complexity:** `O(n * 2^n)`  
- **Accuracy:** ✅ Exact (faster than brute force, but still exponential).

---

### 3. Approximation & Heuristics
Since exact algorithms are infeasible for large `n`, practical methods are used:

| Algorithm                  | Time Complexity | Accuracy |
|-----------------------------|-----------------|----------|
| Nearest Neighbor            | `O(n²)`        | Approximate |
| Minimum Spanning Tree (MST) | `O(n² log n)`  | Approximate |
| Christofides Algorithm      | `O(n³)`        | ≤ 1.5 × Optimal (metric TSP) |
| Metaheuristics (GA, ACO, SA)| Varies         | Good in practice |

---

### Example of Travelling Salesman Problem
graph TD;
    A[City A] -->|10| B[City B]
    A -->|15| C[City C]
    A -->|20| D[City D]
    A -->|25| E[City E]
    A -->|30| F[City F]
    
    B -->|10| A
    B -->|35| C
    B -->|25| D
    B -->|17| E
    B -->|28| F
    
    C -->|15| A
    C -->|35| B
    C -->|30| D
    C -->|28| E
    C -->|40| F
    
    D -->|20| A
    D -->|25| B
    D -->|30| C
    D -->|22| E
    D -->|16| F
    
    E -->|25| A
    E -->|17| B
    E -->|28| C
    E -->|22| D
    E -->|35| F
    
    F -->|30| A
    F -->|28| B
    F -->|40| C
    F -->|16| D
    F -->|35| E



## 🔹 Growth of Complexity Example

| Cities (`n`) | Brute Force Permutations |
|--------------|---------------------------|
| 5            | 24                        |
| 10           | 181,440                   |
| 15           | 43,589,145,600            |
| 20           | ~ 6.08 × 10^16            |

⚡ Complexity grows explosively as `n` increases.

---

## 🔹 Summary

- **TSP is NP-Hard (optimization) and NP-Complete (decision).**
- No polynomial-time algorithm is known for solving TSP exactly.
- Approximation and heuristic methods are widely used in real-world applications (logistics, route planning, circuit design).

---

## 🚀 Applications

- Route planning (delivery, transportation, traveling)
- Circuit design (VLSI layout)
- Genome sequencing (bioinformatics)
- Network optimization

---

## 📖 References
- [Wikipedia: Travelling Salesman Problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
- [Held–Karp Algorithm](https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm)
- [Christofides Algorithm](https://en.wikipedia.org/wiki/Christofides_algorithm)

---
