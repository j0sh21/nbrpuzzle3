
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

sudoku_grid_prisma = [
	[0, 0, 0, 8, 1, 0, 0, 0, 0],
	[4, 0, 0, 0, 5, 6, 0, 3, 2],
	[2, 5, 0, 0, 0, 0, 8, 0, 3],
	[2, 5, 0, 0, 0, 0, 8, 0, 3],
	[0, 0, 4, 0, 7, 0, 9, 0, 0],
	[6, 0, 8, 0, 0, 0, 0, 7, 1],
	[0, 0, 1, 0, 0, 7, 0, 0, 0],
	[7, 2, 0, 3, 8, 0, 0, 0, 9],
	[0, 0, 0, 0, 6, 9, 0, 0, 0]
]

##TODO:

sudoku = [
    [2, 0, 0, 0, 3, 0, 4, 0, 9],
    [0, 4, 0, 8, 0, 7, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 9, 7, 0],
    [1, 0, 7, 0, 0, 0, 0, 9, 8],
    [8, 0, 0, 0, 0, 0, 0, 0, 5],
    [9, 6, 0, 0, 2, 0, 4, 0, 0],
    [0, 0, 4, 3, 0, 1, 0, 0, 0],
    [4, 0, 6, 0, 5, 0, 0, 0, 0],
    [3, 0, 7, 0, 0, 6, 0, 0, 0]
]

asdf = [
    [2, 0, 0, 3, 0, 4, 0, 0, 9],
    [0, 0, 8, 0, 7, 0, 4, 0, 0],
    [0, 4, 0, 8, 0, 9, 0, 7, 0],
    [1, 0, 7, 0, 0, 0, 9, 0, 8],
    [0, 8, 0, 0, 0, 0, 0, 5, 0],
    [9, 0, 6, 0, 0, 0, 2, 0, 4],
    [0, 6, 0, 4, 0, 3, 0, 1, 0],
    [0, 0, 4, 0, 6, 0, 3, 0, 0],
    [3, 0, 0, 7, 0, 5, 0, 0, 6]
]
