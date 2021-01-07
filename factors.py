from math import isqrt


def factors(n):
    factors = []
    for i in range(2, isqrt(n)+1):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    factors = list(set(factors))
    factors.sort()
    return factors


def get_primes(n):
    primes = list(range(2, n+1))
    for i in primes:
        j = 2
        while i * j <= n:
            if i * j in primes:
                primes.remove(i*j)
            j += 1
    return primes

print(get_primes(1000))
