from math import sqrt, ceil
def getDivisors(num):
    if num == 1:
        return 1
    S = 1
    n = ceil(sqrt(num))
    for i in range(2,n):
        if num%i == 0:
            S += i
            S += num//i
    if n **2 == num:
        S += n
    return S

def isAbundant(n):
    return getDivisors(n) > n

#all the abundant numbers under 28123
ab = []
for i in range(1,28123):
    if isAbundant(i):
        ab.append(i)

#understand this
v = [0]*28124
for x in range(len(ab)):
    for y in range(x, len(ab)):
        sum = ab[x] + ab[y]
        if sum <= 28123:
            if v[sum] == 0:
                v[sum] = sum

S = 0
for x in range(len(v)):
    if v[x] == 0:
        S+=x
print(S)
