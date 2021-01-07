def fib(number):
    pre, cur = 0, 1
    for _ in range(number):
        pre, cur = pre + cur, pre
    return pre

i = 1
while True:
    calc = fib(i) 
    if len(str(calc)) == 1000:
        print(i)
        break
    i += 1