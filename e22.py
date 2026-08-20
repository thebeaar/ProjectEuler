arr = []
with open("e22_names.txt", "r") as f:
    for line in f:
        for name in line.split(","):
            arr.append(name.strip('"'))
arr.sort()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

sum = 0
for i, name in enumerate(arr):
    score = 0
    for letter in name:
        score += alphabet.find(letter) + 1
    sum += score * (i+1)

print(sum)