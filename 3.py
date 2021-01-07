from math import isqrt


def check_prime(n):
    S = 2
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            S += 2
    if S == 2:
        return True
    return False

def factors(n):
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            if check_prime(i):
                factor = i
    return factor

print(factors(600851475143))
