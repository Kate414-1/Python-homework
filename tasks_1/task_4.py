def rotate_clockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = []
    for j in range(m):
        new_row = []
        for i in range(n - 1, -1, -1):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result

def rotate_counterclockwise(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = []
    for j in range(m - 1, -1, -1):
        new_row = []
        for i in range(n):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(' '.join(map(str,row)))
    print()

print_matrix([[1,2,3],[4,5,6]])
print_matrix(rotate_clockwise([[1,2,3],[4,5,6]]))
print_matrix(rotate_counterclockwise([[1,2,3],[4,5,6]]))
print('---------')
print_matrix([[1,2],[4,5],[7,8]])
print_matrix(rotate_clockwise([[1,2],[4,5],[7,8]]))
print_matrix(rotate_counterclockwise([[1,2],[4,5],[7,8]]))