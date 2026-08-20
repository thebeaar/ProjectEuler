def sum_divs(n):
    sum = 0
    for div in range(1, n):
        if n % div == 0:
            sum+=div
    return sum

dictionary = {}
arr = set()


for i in range(1, 10_000):
    n = sum_divs(i)
    if n in dictionary.keys() and dictionary[n] == i:
        arr.add(n)
        arr.add(i)
    else:
        dictionary[i] = n

sum = 0
for i in arr:
    sum += i
print(sum)


