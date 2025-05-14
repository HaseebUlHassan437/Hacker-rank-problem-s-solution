# 🧠 Queen's Attack II – HackerRank Solution

This repository contains a Python solution to the **"Queen's Attack II"** problem from [HackerRank](https://www.hackerrank.com/challenges/queens-attack-2). It calculates the number of squares a queen can attack on an `n x n` chessboard, taking into account obstacles.

## 📝 Problem Statement

The queen is standing at position `(r_q, c_q)` on an `n x n` chessboard. There are `k` obstacles on the board. The queen can move:

- Vertically (up/down)
- Horizontally (left/right)
- Diagonally (all 4 directions)

An obstacle blocks the queen's movement in that direction beyond its position.

### Input

- `n`: Size of the chessboard (n x n)
- `k`: Number of obstacles
- `r_q, c_q`: Position of the queen
- `obstacles`: List of positions that contain obstacles

### Output

- Number of cells the queen can attack

## 🚀 Approach

1. **Direction-Based Analysis**: The board is divided into 8 directions (U, D, L, R, UL, UR, DL, DR).
2. **Obstacle Filtering**: For each obstacle, determine its direction relative to the queen.
3. **Blocked Cells Tracking**: Simulate how far the queen can go in each direction until an obstacle or edge is hit.
4. **Efficient Computation**: Return total attackable cells by subtracting blocked cells from max possible moves.

## 📁 Files

- `queens_attack.py`: Main Python script solving the problem
- `README.md`: This file

## 🛠️ Technologies

- Python 3
- HackerRank I/O structure

## 💡 Sample Input
```

n = 5
k = 3
r\_q = 4
c\_q = 3
obstacles = \[\[5,5], \[4,2], \[2,3]]

```

## ✅ Sample Output
```

10

```

## 🔗 HackerRank Link

Solve this problem on HackerRank:  
[https://www.hackerrank.com/challenges/queens-attack-2](https://www.hackerrank.com/challenges/queens-attack-2)

## 📚 License

This repository is open-sourced under the MIT License.

---

### 👨‍💻 Author

- [Haseeb Ul Hassan](https://github.com/HaseebUlHassan437)


