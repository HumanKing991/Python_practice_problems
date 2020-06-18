def rotate(matrix):
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    print(matrix)

som = int(input('Enter The Size Of Matrix : '))
matrix = [[int(x) for x in input().split()]for i in range(som)]
rotate(matrix)
