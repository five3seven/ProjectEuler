from math import log10
number = open('number.txt','r')
bsnumber = []
for i in range(100):
    bsnumber.append([])
    for n in number.readline().split():
        bsnumber[i].append(n)

def first_n_digits(number, x):
    return number // 10 ** int(log10(number)-x + 1)

def sum(numbers):
    S = 0
    for i in range(len(numbers)):
        S+=int(numbers[i][0])
    return first_n_digits(S, 10)


print(sum(bsnumber))