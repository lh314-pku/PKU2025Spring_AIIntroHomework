# 将罗马数字转化为整型
def change_roman_to_int(roman):

    # 用字典存储各符号对应的值
    map_symbols = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    ans = 0
    for i in range(len(roman)):
        if i > 0 and map_symbols[roman[i]] > map_symbols[roman[i - 1]]:
            ans += map_symbols[roman[i]] - 2 * map_symbols[roman[i - 1]]
        else:
            ans += map_symbols[roman[i]]
    return ans


roman_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
             (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def change_int_to_roman(num):
    res = ''
    while num > 0:
        for i, r in roman_map:
            while num >= i:
                res += r
                num -= i
    return res

r = input()
if '0' <= r[0] <= '9':
    r = int(r)
    print(change_int_to_roman(r))
else:
    print(change_roman_to_int(r))