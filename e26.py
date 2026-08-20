def long_div_repeats(n):
    arr = []
    s = 1
    while s != 0 and s not in arr:
        arr.append(s)
        s = (s%n) * 10
    if s == 0:
        return 0
    return len(arr) - arr.index(s)


maxlength = 0
maxI = 1
for i in range(2, 1000):
    l = long_div_repeats(i)
    if l > maxlength:
        maxlength = l
        maxI = i
print(maxI)
