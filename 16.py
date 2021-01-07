def power_digit_sum(power):
    number = 2**power
    S = 0
    while number != 0:
        S += number % 10
        number //= 10
    return S

print(power_digit_sum(1000))