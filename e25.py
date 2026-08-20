def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

i = 1
while fibonacci(i) < 10**999:
    i+=1
print(i)