from math import isqrt
def divisorSum(number):
    S = 1
    for i in range(2,isqrt(number)):
        if number % i == 0:
            S += i + number//i
    return S

def checkAmicable(number):
    return number == divisorSum(divisorSum(number))
    
def difAm(number):
    return number != divisorSum(number)

S = 0
for i in range(10000):
    if checkAmicable(i) and difAm(i):
        S += divisorSum(divisorSum(i))
print(S)