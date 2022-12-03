input = open("input.txt", "r")

count = 0

for line in input:
    line = line.split(" | ")
    line[1] = line[1].strip()
    outputValues = line[1].split(" ")
    for output in outputValues:
        if len(output) in (2, 3, 4, 7):
            count += 1
print(count)
