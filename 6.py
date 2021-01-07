def sum_sqr(lim):
    S = 1
    for i in range(2, lim+1):
        S += i ** 2
    return S


def sqr_sum(lim):
    S = 1
    for i in range(2, lim+1):
        S += i
    return S**2


print(sum_sqr(10))
