file = open("input.txt", "r")

previous = int(file.readline())
count = 0

for line in file:
    if int(line) > previous:
        count += 1

    previous = int(line)

print(count)
