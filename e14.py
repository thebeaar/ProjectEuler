def play(n):
    if n % 2 == 0:
        return n//2
    else:
        return n*3 + 1

maxLength = 0
maxNum = 1
for i in range(1, 1_000_000):
    print(i)
    n = i
    count = 0
    while n != 1:
        n = play(n)
        count += 1
    if count > maxLength:
        maxLength = count
        maxNum = i

print(maxNum)