ll = list(map(int, input().split()))
max_odd, min_even = 0, 200
for i in range(6):
    if ll[i] % 2 == 1:
        if ll[i] > max_odd:
            max_odd = ll[i]
    else:
        if ll[i] < min_even:
            min_even = ll[i]
print(abs(max_odd - min_even))