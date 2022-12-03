file = open("input.txt", "r")

lines = []
count = 0

for line in file:
    lines.append(int(line.strip()))

prevSum = lines[0] + lines[1] + lines[2]
newSum = prevSum

for i in range(3, 2000):
    newSum -= lines[i-3]
    newSum += lines[i]
    if newSum > prevSum:
        count += 1

    prevSum = newSum

print(count)
