def multiple_sum(n1, n2, limit):
    sum = 0
    number = 1
    while True:
        if number == limit:
            break
        if number % n1 == 0 or number % n2 == 0:
            sum += number
        number += 1
    return sum

print(multiple_sum(3, 5, 1000))