def harmonic_frac(n):
    top = 0
    bottom = 1
    for k in range(1, n+1):
        top += k * bottom
        bottom *= k

        ##top, bottom = make_smaller(top, bottom)
    return make_smaller(top, bottom)

def make_smaller(t, b):
    div = 2
    while  t > 1 and b > 1:
        if t % div == 0 and b % div == 0:
            t //= div
            b //= div
        else:
            div += 1
    return t, b

print(make_smaller(8, 2))
print(make_smaller(110, 30))

for i in range(1_000_000, 1_000_000_000):
    _, b = harmonic_frac(i)
    print(b)
    if b % 137 != 0:
        print(i)