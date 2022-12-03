file = open("input.txt", "r")

numbers = []

for line in file:
    numbers.append(list(map(int, line.strip())))

count = 0
riskLevel = 0

# Inner Numbers
for x in range(1, len(numbers)-1):
    for y in range(1, len(numbers[x])-1):
        if numbers[x][y] < numbers[x][y-1] and numbers[x][y] < numbers[x+1][y] and numbers[x][y] < numbers[x-1][y] and numbers[x][y] < numbers[x][y+1]:
            riskLevel += (numbers[x][y] + 1)
            count += 1

print("Count:", count)
print("Risk:", riskLevel)
