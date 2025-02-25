n, k = map(int, input().split())
found = False
for m in range(1, 21):
    price = 200 * (1 + k/100) ** (m-1)
    savings = n * m
    if savings >= price:
        print(m)
        found = True
        break
if not found:
    print("Impossible")