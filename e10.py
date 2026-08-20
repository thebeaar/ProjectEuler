import math
def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
upper = 2000000
sum = 0

for i in range(2,upper):
    if is_prime(i):
        sum += i
print(sum)