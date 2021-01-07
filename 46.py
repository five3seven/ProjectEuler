from math import isqrt


def is_prime(n):
    if n in [0, 1]:
        return False
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            return False
    return True


def check_goldbach(n):
    for pr in range(1, isqrt(n)):
        pr = n - 2 * pr ** 2
        if pr < 0:
            break
        if is_prime(pr):
            return True
    return False


i = 33
while True:
    if not is_prime(i) and not check_goldbach(i):
        print(i)
        break
    i += 2
