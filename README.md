# 🧮 Matrix Dominant Cell Detector
A simple **Python project** that counts the number of *dominant cells* in a matrix.

---

## 📖 What is a Dominant Cell?
A **dominant cell** is a cell whose value is **strictly greater than all its 8 neighboring cells** (top, bottom, left, right, and the four diagonals).

**Example:**
| 4 | 5 | 6 |
|---|---|---|
| 3 | 9 | 2 |
| 1 | 8 | 7 |

In this example, **9** is a dominant cell because it is greater than all the surrounding values.

---

## 🚀 How It Works
1. The program takes a 2D grid (matrix) as input.  
2. It compares each element with all possible 8 neighbors.  
3. It counts how many cells are **dominant** (greater than all their neighbors).  
4. Finally, it prints the total count.

---

## 🧩 Input Format
```
grid_rows
grid_columns
matrix_elements
```

**Example Input:**
```
3
3
4 5 6
3 9 2
1 8 7
```

**Example Output:**
```
1
```

---

## 🧠 Example Explanation
Input:
```
3
3
4 5 6
3 9 2
1 8 7
```
Explanation: Only **9** is greater than all its neighboring cells.  
Hence, output = **1**

---

## 🖥️ How to Run
1. Open a terminal or command prompt.  
2. Run the Python file:
   ```
   python3 matrix_dominant_cell.py
   ```
3. Enter your input when prompted.  
4. The program will print the number of dominant cells.

---

## 🧾 Code Reference
```
def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0
    for i in range(n):
        for j in range(m):
            cell_value = grid[i][j]
            is_dominant = True
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ni = i + dx
                    nj = j + dy
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] >= cell_value:
                        is_dominant = False
                        break
                if not is_dominant:
                    break
            if is_dominant:
                count += 1
    return count
```

---

## 📄 License
This project is open-source and free to use for educational purposes.  
Feel free to modify and improve it.

---

## ✨ Author
**Rimjhim Rawat**  
🎓 CSE (Blockchain Technology), SRM University  
💻 Beginner Python Developer
