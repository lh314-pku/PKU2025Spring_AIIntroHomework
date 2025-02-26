k = int(input())
# 辗转相除法
def gcd(m, n):
    if m % n == 0:
        return n
    else:
        q = m // n
        r = m % n
        return gcd(n, r)

for i in range(k):
    m, n = map(int, input().split())
    print(gcd(m, n))
