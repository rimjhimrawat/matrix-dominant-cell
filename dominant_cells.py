import math
import os
import sys

def numCells(grid):
    n = len(grid)
    m = len(grid[0])
    count = 0

    for i in range(n):
        for j in range(m):
            cell_value = grid[i][j]
            is_dominant = True

            # Check all 8 neighbors
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if dx == 0 and dy == 0:
                        continue
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] >= cell_value:
                        is_dominant = False
                        break
                if not is_dominant:
                    break

            if is_dominant:
                count += 1
    return count

if __name__ == '__main__':
    grid_rows = int(input("Enter number of rows: ").strip())
    grid_columns = int(input("Enter number of columns: ").strip())

    grid = []
    print("Enter grid rows:")
    for _ in range(grid_rows):
        grid.append(list(map(int, input().strip().split())))

    result = numCells(grid)
    print("Dominant cells count:", result)
