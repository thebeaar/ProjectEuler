def triag(n):
    return ((n+1) * n) / 2
def num_devisors(n):
    divs = []
    dt = {}
    div = 2
    while n > 1:
        if n % div == 0:
            if div in divs:
                dt[div] += 1
            else:
                dt[div] = 1
                divs.append(div)
            n /= div
        else:
            div += 1

    numDivs = 1

    for div in divs:
        numDivs *= (1 + dt[div])
    return numDivs

i = 1

while num_devisors(triag(i)) < 500:
    i += 1
print(triag(i))