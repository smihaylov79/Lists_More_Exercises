def check_the_winner(grid, player):
    full_list_for_check=[]
    for row in grid:
        for i in range(3):
            full_list_for_check.append(row[i])
    for rows in range(3):
        for cols in grid:
            full_list_for_check.append(cols[rows])
    row_diagonal_1 = 0
    row_diagonal_2 = 2
    for cols_diagonal in grid:
        full_list_for_check.append(cols_diagonal[row_diagonal_1])
        row_diagonal_1 += 1
    for cols_diagonal in grid:
        full_list_for_check.append(cols_diagonal[row_diagonal_2])
        row_diagonal_2 -= 1
    full_list_for_check=[full_list_for_check[:3]]+[full_list_for_check[3:6]]+\
                        [full_list_for_check[6:9]]+[full_list_for_check[9:12]]+\
                        [full_list_for_check[12:15]]+[full_list_for_check[15:18]]+\
                        [full_list_for_check[18:21]]+[full_list_for_check[21:24]]
    for item in full_list_for_check:
        if item.count(player) == 3:
            return True

table = []
for i in range(3):
    table.append(str.split(input()))
if check_the_winner(table, '1'):
    print('First player won')
elif check_the_winner(table, '2'):
    print('Second player won')
else:
    print('Draw!')
