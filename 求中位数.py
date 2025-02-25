n = int(input())
nnn = input().split()
nums = []
for i in range(n):
    nums.append(int(nnn[i]))

nums.sort()

if n % 2 == 0:
    ind = (nums[n // 2] + nums[n // 2 - 1])
    if ind % 2 == 0:
        print(ind // 2)
    else:
        print(ind / 2)
else:
    print(nums[(n - 1) // 2])