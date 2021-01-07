def factorial(number):
    f = 1
    for i in range(1,number+1):
        f*=i
    return f

def latticePaths(grid):
    n = grid * 2
    k = grid
    C = factorial(n)//(factorial(k)*factorial(n - k))
    return C

print(latticePaths(20))
