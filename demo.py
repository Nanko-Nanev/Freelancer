def read_matrix():
    size = int(input())
    matrix = []
    for row in range(size):
        row = [int(x) for x in input().split()]
        matrix.append(row)
    return matrix


def is_valid_range(row_coordinate, column_coordinate, size):
    if 0 <= row_coordinate < size and 0 <= column_coordinate < size:
        return True
    return False


def bomb_explosion(bombs, matrix):
    row, column = [int(x) for x in bombs.split(",")]
    bomb_range = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
    for row_step, column_step in bomb_range:
        potential_row = row + row_step
        potential_column = column + column_step
        if is_valid_range(potential_row, potential_column, len(matrix)):
            if matrix[potential_row][potential_column] > 0:
                matrix[potential_row][potential_column] -= matrix[row][column]
    if matrix[row][column] > 0:
        matrix[row][column] = 0
    return matrix


def print_result(matrix):
    alive_cells = 0
    cells_sum = 0
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            if matrix[row][column] > 0:
                alive_cells += 1
                cells_sum += matrix[row][column]
    print(f"Alive cells: {alive_cells}")
    print(f"Sum: {cells_sum}")
    for row in range(len(matrix)):
       print(" ".join(str(x) for x in matrix[row]))


matrix = read_matrix()
bombs = input().split()

for bomb in range(len(bombs)):
    bomb_explosion(bombs[bomb], matrix)

print_result(matrix)