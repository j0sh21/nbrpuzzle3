
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

grid_2 = [
    [0, 9, 0, 4, 0, 0, 0, 0, 0],
    [7, 2, 6, 1, 5, 0, 0, 0, 0],
    [6, 0, 0, 0, 0, 0, 8, 0, 0],
    [8, 9, 0, 0, 1, 0, 2, 0, 3],
    [0, 7, 0, 6, 0, 3, 0, 9, 0],
    [4, 5, 0, 9, 0, 1, 6, 0, 0],
    [0, 4, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 1, 0, 5, 8, 6, 0, 0],
    [0, 0, 0, 4, 9, 0, 0, 0, 0]
]

# Aufgabenstellung (Puzzle Grid)
grid_3 = [
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 1, 0, 0, 0, 0, 4],
    [6, 0, 0, 0, 3, 0, 0, 2, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 2],
    [0, 0, 8, 0, 0, 0, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 3, 5, 0],
    [0, 0, 0, 0, 0, 3, 0, 6, 0],
    [0, 0, 0, 0, 0, 9, 0, 0, 0]
]

# Lösung (Solution Grid)
solution_grid_3 = [
    [9, 1, 3, 2, 4, 5, 6, 7, 8],
    [5, 2, 7, 1, 6, 8, 9, 3, 4],
    [6, 8, 4, 9, 3, 7, 1, 2, 5],
    [2, 3, 1, 5, 7, 4, 8, 9, 6],
    [7, 6, 9, 3, 8, 1, 5, 4, 2],
    [4, 5, 8, 6, 9, 2, 7, 1, 3],
    [8, 7, 2, 4, 1, 6, 3, 5, 9],
    [1, 9, 5, 8, 2, 3, 4, 6, 7],
    [3, 4, 6, 7, 5, 9, 2, 8, 1]
]

easy_sudoku = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

sudoku_with_several_solutions = [
    [0, 0, 0, 0, 5, 0, 2, 0, 0],
    [0, 0, 0, 0, 4, 7, 9, 0, 0],
    [1, 0, 5, 0, 0, 8, 0, 0, 0],
    [2, 4, 0, 0, 0, 0, 0, 9, 0],
    [3, 0, 7, 0, 0, 0, 0, 4, 6],
    [0, 0, 0, 7, 0, 0, 7, 5, 3],
    [0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 2, 1, 5, 9, 0, 0, 0],
    [0, 0, 4, 7, 0, 0, 0, 0, 0]
]

def print_rows(task_p):
    lines = []
    for line_number, line in enumerate(task_p):
        print(f"Zeile: {line_number+1}   {line}")
        lines.append(line)
    return lines

def print_cols(task_p):
    columns = []
    horizontal_grid = zip(*task_p)
    for line_number, colum in enumerate(horizontal_grid):
        print(f"Spalte: {line_number+1}   {colum}")
        columns.append(colum)
    return columns


def print_squares(grid):
    squares = []
    for block_row in range(3):
        for block_col in range(3):
            square = []
            for row in range(3):
                for col in range(3):
                    square.append(grid[block_row * 3 + row][block_col * 3 + col])
            squares.append(square)

    for square_number, square in enumerate(squares):
        print(f"Quadrat {square_number + 1}: {square}")
    return squares

def show_sudoku(puzzle):
    rows = print_rows(puzzle)
    columns = print_cols(puzzle)
    squares = print_squares(puzzle)

    for row in rows:
        missing = []
        if 1 not in row:
            missing.append(1)
        if 2 not in row:
            missing.append(2)
        if 3 not in row:
            missing.append(3)
        if 4 not in row:
            missing.append(4)
        if 5 not in row:
            missing.append(5)
        if 6 not in row:
            missing.append(6)
        if 7 not in row:
            missing.append(7)
        if 8 not in row:
            missing.append(8)
        if 9 not in row:
            missing.append(9)
        print(f"Es fehlen in der Zeile {({rows.index(row)})}: {len(missing)} Werte, nämlich: {missing}")

    for column in columns:
        missing_c = []
        if 1 not in column:
            missing_c.append(1)
        if 2 not in column:
            missing_c.append(2)
        if 3 not in column:
            missing_c.append(3)
        if 4 not in column:
            missing_c.append(4)
        if 5 not in column:
            missing_c.append(5)
        if 6 not in column:
            missing_c.append(6)
        if 7 not in column:
            missing_c.append(7)
        if 8 not in column:
            missing_c.append(8)
        if 9 not in column:
            missing_c.append(9)
        print(f"Es fehlen in der Spalte {({columns.index(column)})}: {len(missing_c)} Werte, nämlich: {missing_c}")

    for square in squares:
        missing_s = []
        if 1 not in square:
            missing_s.append(1)
        if 2 not in square:
            missing_s.append(2)
        if 3 not in square:
            missing_s.append(3)
        if 4 not in square:
            missing_s.append(4)
        if 5 not in square:
            missing_s.append(5)
        if 6 not in square:
            missing_s.append(6)
        if 7 not in square:
            missing_s.append(7)
        if 8 not in square:
            missing_s.append(8)
        if 9 not in square:
            missing_s.append(9)
        print(f"Es fehlen im Quardrat {({squares.index(square)})}: {len(missing_s)} Werte, nämlich: {missing_s}")



if __name__ == "__main__":
    show_sudoku(grid)
