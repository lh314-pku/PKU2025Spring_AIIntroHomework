k = int(input())
for i in range(k):
    a, b = map(int, input().split())
    print(a + b)

# 其实大整数加法肯定不是这样写的
# 但是 Python 很神奇的就 AC 了
# 可能是因为Python的整型数据类型int在存储上是没有限制范围的
# 导致 '+' 可以直接处理大整数加法