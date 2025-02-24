strs = input()
str1, str2 = strs.split(' ')
if len(str2) <= len(str1):
    print(str1 + str2)
else:
    print(str2 + str1)