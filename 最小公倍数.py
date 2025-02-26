m, n = map(int,input().split(','))
x = m * n
# 先求最大公约数（辗转相除法）
if m < n:
    n = m + n
    m = n - m
    n = n - m

def gcd(m, n):
    if m % n == 0:
        return n
    else:
        q = m // n
        r = m % n
        return gcd(n, r)
# 使用公式 lcm(a, b) = (a * b) / gcd(a, b)
print(x // gcd(m, n))