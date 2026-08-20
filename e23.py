def sum_divs(n):
    sum = 0
    for div in range(1, n//2 + 1):
        if n % div == 0:
            sum+=div
    return sum

def is_abundant(n):
    return sum_divs(n) > n

sum = 0

arr = []
for i in range(1, 28_123):
    print(i)
    if is_abundant(i):
        arr.append(i)
arr.sort()

print(arr)

for i in range(1, 28123):
    l = 0
    r = len(arr)-1
    while l <= r and arr[l] + arr[r] != i:
        if arr[l] + arr[r] < i:
            l = l+1
        else:
            r = r-1
    if l > r:
        sum += i
        print(i)
print(sum)