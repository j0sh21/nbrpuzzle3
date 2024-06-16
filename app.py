import puzzless
def print_rows(task_p):
    lines = []
    for line_number, line in enumerate(task_p):
        print(f"Zeile  : {line_number+1}   {line}")
        lines.append(line)
    print("\n")
    return lines

def print_cols(task_p):
    columns = []
    horizontal_grid = zip(*task_p)
    for line_number, colum in enumerate(horizontal_grid):
        print(f"Spalte : {line_number+1}  {colum}")
        columns.append(colum)
    print("\n")
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
        print(f"Quadrat: {square_number + 1} {square}")
    return squares

def show_sudoku(puzzle):
    rows = print_rows(puzzle)
    columns = print_cols(puzzle)
    squares = print_squares(puzzle)
    print("\n__________Missing Values______________\n")
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
        print(f"Z: {({rows.index(row)})}  {len(missing)} V: {missing}")
    print(f'{"_" * 39}')
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
        print(f"S: {({columns.index(column)})}  {len(missing_c)}V: {missing_c}")
    print(f'{"_"*39}')
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
        print(f"Q: {({squares.index(square)})}  {len(missing_s)}V: {missing_s}")
    print(f'{"_"*39}')
    return missing, missing_c, missing_s

if __name__ == "__main__":
    a, b, c = show_sudoku(puzzless.asdf)