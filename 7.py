from math import isqrt


def check_prime(n):
    S = 2
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            S += 2
    if S == 2:
        return True
    return False


p = 1
count = 0
while True:
    if check_prime(p):
        count += 1
    if count == 10001:
        print(p)
        break
    p += 2
