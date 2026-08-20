def num_letter(n):
    dictionaryTeens = {0:0, 1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:9, 19:8}
    dictionaryTens = {2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
    s = str(n)
    if n == 1000:
        return 11
    numLetters = 0
    if n % 100 != 0 and n > 100:
        numLetters = 3
    if (n // 10) % 10 <= 1:
        numLetters += dictionaryTeens[n % 100]
    else:
        numLetters += dictionaryTens[(n // 10) % 10]
        numLetters += dictionaryTeens[n % 10]
    if n > 100:
        numLetters += dictionaryTeens[n // 100] + 7
    return numLetters

sum = 0
for n in range(1, 1001):
    sum += num_letter(n)
print(sum)