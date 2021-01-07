from math import isqrt


def get_primes(n):
    primes = list(range(2, n+1))
    for i in primes:
        j = 2
        while i*j <= primes[-1]:
            if i*j in primes:
                primes.remove(i*j)
            j += 1
    return primes


def goldbach(n):
    prime_list = get_primes(n)
    if n in prime_list or n % 2 == 0:
        return True
    for pr in prime_list:
        for i in range(isqrt(n)):
            if pr + 2 * i ** 2 == n:
                return True
    return True


i = 33
while True:
    if not goldbach(i):
        print(i)
        break
    print(i)
    i += 2
