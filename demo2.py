n = int(input())
matrix = []
list_of_bomb_coordinates = []
damage_r = [-1, -1, -1, 0, 0, 1, 1, 1]
damage_c = [-1, 0, 1, -1, 1, -1, 0, 1]
alive_cells_sum = 0
alive_cells_count = 0

for _ in range(n):
    add_current_row = [int(x) for x in input().split()]
    matrix.append(add_current_row)

bomb_coordinates = input().split()
for coord_row in bomb_coordinates:
    row, col = [int(x) for x in coord_row.split(",")]
    list_of_bomb_coordinates.append([row, col])

for coordinate in list_of_bomb_coordinates:
    bomb_r = coordinate[0]
    bomb_c = coordinate[1]
    bomb_value = matrix[bomb_r][bomb_c]
    if bomb_value <= 0:
        continue
    else:
        matrix[bomb_r][bomb_c] = 0
        for i in range(len(damage_r)):
            row_index_dmg = bomb_r + damage_r[i]
            col_index_dmg = bomb_c + damage_c[i]
            bomb_index_checker = [row_index_dmg, col_index_dmg]
            if 0 <= row_index_dmg < n and 0 <= col_index_dmg < n:
                # if bomb_index_checker not in list_of_bomb_coordinates:
                if matrix[row_index_dmg][col_index_dmg] > 0:
                    matrix[row_index_dmg][col_index_dmg] -= bomb_value

for r in range(n):
    for c in range(n):
        if matrix[r][c] > 0:
            alive_cells_count += 1
            alive_cells_sum += matrix[r][c]
print(f"Alive cells: {alive_cells_count}")
print(f"Sum: {alive_cells_sum}")

for row_matrix in matrix:
    print(*row_matrix)