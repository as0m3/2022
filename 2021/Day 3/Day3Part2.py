file = open("input.txt", "r")

lines = []

for line in file:
    lines.append(line.strip())


def oxygenGeneratorRating(list: list, index: int):
    count1 = 0
    newList = []
    for i in range(len(list)):
        if list[i][index] == "0":
            count1 += 1

    for i in range(len(list)):
        if count1 > (len(list)/2):  # 0 more than half of the time
            if list[i][index] == "0":
                newList.append(list[i])
        else:  # otherwise 1 more than half of the time
            if list[i][index] == "1":
                newList.append(list[i])

    if len(newList) != 1:
        return oxygenGeneratorRating(newList, index+1)
    else:
        return newList


def co2GeneratorRating(list: list, index: int):
    count2 = 0
    newList = []
    for i in range(len(list)):
        if list[i][index] == "0":
            count2 += 1

    for i in range(len(list)):
        if count2 <= (len(list)/2):  # 0 less than half of the time
            if list[i][index] == "0":
                newList.append(list[i])
        else:  # otherwise 1 less than half of the time
            if list[i][index] == "1":
                newList.append(list[i])

    if len(newList) != 1:
        return co2GeneratorRating(newList, index+1)
    else:
        return newList


o2Rate = oxygenGeneratorRating(lines, 0)
co2Rate = co2GeneratorRating(lines, 0)

lifeSupportRating = int(o2Rate[0], 2) * int(co2Rate[0], 2)
print(lifeSupportRating)
