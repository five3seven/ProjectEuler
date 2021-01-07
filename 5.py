def is_div(n, m=20):
    for i in range(2, m+1):
        if n % i != 0:
            return False
    return True

p = 20
while True:
    if is_div(p):
        print(p)
        break
    p += 20
