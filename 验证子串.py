to_find = input()
strs = input()
if to_find in strs:
    print(f"{to_find} is substring of {strs}")
elif strs in to_find:
    print(f"{strs} is substring of {to_find}")
else:
    print("No substring")