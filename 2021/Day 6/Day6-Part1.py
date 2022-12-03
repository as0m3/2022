input = open("input.txt", "r")

ages = input.readline().split(",")
ages = [int(i) for i in ages]
#         0  1  2  3  4  5  6  7  8
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for age in ages:
    counts[age] += 1

days = 1

while days <= 256:
    temp = counts[0]
    counts[0] = counts[1]
    counts[1] = counts[2]
    counts[2] = counts[3]
    counts[3] = counts[4]
    counts[4] = counts[5]
    counts[5] = counts[6]
    counts[6] = counts[7]+temp
    counts[7] = counts[8]
    counts[8] = temp

    days += 1

print(sum(counts))
