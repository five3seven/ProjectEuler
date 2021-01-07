def check_palindrome(n):
    p = n
    c = 0
    while n != 0:
        c = c * 10 + n % 10
        n //= 10
    return c == p


def larget_palindrome(llim, hlim):
    p = 0
    for i in range(llim, hlim+1):
        for j in range(llim, hlim+1):
            if check_palindrome(i * j) and i * j > p:
                p = i * j
    return p


print(larget_palindrome(100, 999))
