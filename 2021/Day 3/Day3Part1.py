file = open("input.txt", "r")

lines = []
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
gamma = ""
epsilon = ""

for line in file:
    lines.append(line.strip())

for i in range(1000):
    for j in range(12):
        if lines[i][j] == "0":
            counts[j] += 1

for i in range(12):
    if counts[i] > 500:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

result = int(gamma, 2) * int(epsilon, 2)
print(result)
print(counts)
print(gamma)
