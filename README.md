# nbrpuzzle3
Solving app for number games. v 0.0.1 pre, pre alpha

## In Development not finished YET!

### Sudoku Solver Summary

1. **System**: The Sudoku grid is divided into 9 large squares (A to I) with rows and columns labeled 1 to 9.

2. **Approach**: We use a Python program to solve the Sudoku by filling empty cells while following Sudoku rules (no repeating numbers in any row, column, or 3x3 square).

3. **Example Grid**:
    ```python
    grid = [
        [3, 1, 0, 0, 0, 2, 3, 9, 6],
        [6, 2, 5, 1, 0, 0, 0, 3, 7],
        [8, 0, 0, 5, 3, 9, 6, 4, 0],
        [9, 1, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 7, 6, 2, 3, 9, 6, 1],
        [1, 3, 0, 9, 5, 4, 2, 0, 0],
        [7, 9, 6, 0, 8, 1, 5, 3, 2],
        [0, 0, 8, 4, 0, 0, 0, 7, 5],
        [0, 5, 0, 0, 7, 6, 1, 8, 9]
    ]
    ```

4. **Solving Algorithm**: The backtracking algorithm is used to fill in the missing numbers.

5. **Code**:
    ```python
    def print_grid(grid):
        for row in grid:
            print(" ".join(str(num) for num in row))

    def find_empty_location(grid, l):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == 0:
                    l[0], l[1] = row, col
                    return True
        return False

    def used_in_row(grid, row, num):
        return num in grid[row]

    def used_in_col(grid, col, num):
        return any(grid[row][col] == num for row in range(9))

    def used_in_box(grid, row, col, num):
        box_row_start, box_col_start = row - row % 3, col - col % 3
        return any(grid[i][j] == num for i in range(box_row_start, box_row_start + 3) for j in range(box_col_start, box_col_start + 3))

    def is_safe(grid, row, col, num):
        return not used_in_row(grid, row, num) and not used_in_col(grid, col, num) and not used_in_box(grid, row, col, num)

    def solve_sudoku(grid):
        l = [0, 0]
        if not find_empty_location(grid, l):
            return True

        row, col = l[0], l[1]

        for num in range(1, 10):
            if is_safe(grid, row, col, num):
                grid[row][col] = num
                if solve_sudoku(grid):
                    return True
                grid[row][col] = 0

        return False

    if solve_sudoku(grid):
        print("Sudoku solved successfully!")
        print_grid(grid)
    else:
        print("No solution exists.")
    ```

This code helps the computer to solve the Sudoku puzzle by checking which numbers fit into each empty cell.
