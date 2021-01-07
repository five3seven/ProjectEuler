def factorial(number):
    f = 1
    for i in range(1, number+1):
        f *= i
    return f

def digitSum(number):
    S = 0
    for _ in range(len(str(number))):
        S += number % 10
        number = number // 10
    return S

print(digitSum(factorial(100)))