def fib_sequence(limit):
    pre, cur = 1, 1
    S = 0
    while pre <= limit:
        pre, cur = cur, pre + cur
        if pre % 2 == 0:
            S += pre
    print(S)

fib_sequence(4000000)