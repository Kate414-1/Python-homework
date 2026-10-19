def create_chess_matrix(n, m, first_symbol, second_symbol):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            if (i + j) % 2 == 0:
                row.append(first_symbol)
            else:
                row.append(second_symbol)
        matrix.append(row)
    return matrix

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))
    print()

print("Режим 1: числа 0 и 1")
print_matrix(create_chess_matrix(3, 5, 0, 1))

print("Режим 2: символы '-' и '+'")
print_matrix(create_chess_matrix(2, 4, '-', '+'))

print("Режим 3: начать с 1")
print_matrix(create_chess_matrix(3, 3, 1, 0))

print("Режим 4: 4 × 2, символы 'X' и 'O'")
print_matrix(create_chess_matrix(4, 2, 'X', 'O'))