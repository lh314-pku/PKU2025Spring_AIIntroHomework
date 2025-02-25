ll = input().split()
n = len(ll)
for i in range(n):
    if i != n - 1:
        print(ll[n - i - 1], end = ' ')
    else:
        print(ll[n - i - 1])