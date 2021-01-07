m = open('path.txt','r')
matrix = []

for i in range(100):
    matrix.append([])
    for x in m.readline().split():
        matrix[i].append(int(x))

def matrix_path(matrix):
    while len(matrix) != 1:
        for i in range(len(matrix[-2])):
            matrix[-2][i] += max(matrix[-1][i], matrix[-1][i+1])
        matrix.pop(-1)
    return matrix[0]

print(matrix_path(matrix))