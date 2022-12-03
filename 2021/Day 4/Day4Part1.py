file = open("input.txt", "r")

# Numbers to be called
numbers = file.readline()
numbers = numbers.split(",")
bingoNumbers = []
for number in numbers:
    bingoNumbers.append(number.strip())

lines = []
bingoLine = 0

count = 0
for line in file:
    if line == "\n":
        lines.append("==============")
    else:
        lines.append(line.strip())

for i in range(len(lines)):
    lines[i] = lines[i].split(" ")
    newList = []
    for j in range(len(lines[i])):
        if lines[i][j] != "":
            newList.append(lines[i][j])
    lines[i] = newList


def bingoCall(number: str):
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == number:
                lines[i][j] = "*"


def bingoCheck(lastNumber: int):
    # horizontal check
    for i in range(len(lines)):
        isBingo = True
        for j in range(len(lines[i])):
            if lines[i][j] != "*":
                isBingo = False
                break
        if isBingo == True:
            print("\nHorizontal Bingo: Line: " + str(i))
            scoreBingo(i, lastNumber)
            return True

    # if here, there were no horizontal bingos
    # check vertical
    for i in range(600):
        if lines[i][0] == "==============":
            # check vertical lines for bingos
            for y in range(5):
                isBingo = True
                for x in range(1, 6):
                    if lines[i+x][y] != "*":
                        isBingo = False
                        break
                if isBingo == True:
                    print("\nVertical Bingo: Line: " +
                          str(i) + " - Column: " + str(y))
                    scoreBingo(i, lastNumber)
                    return True
        i += 5
    return False


def printBoards():
    for i in range(len(lines)):
        print(lines[i])


def scoreBingo(lineNumber: int, lastNumber: int):
    score = 0
    for i in range(1, 6):
        print(lines[lineNumber+i])
        for j in range(5):
            if lines[lineNumber+i][j] != "*":
                score += int(lines[lineNumber+i][j])
    score *= int(lastNumber)
    print("\nScore: " + str(score) + "\n")


def bingoLoop():
    bingo = False
    for i in range(len(bingoNumbers)):
        bingoCall(bingoNumbers[i])
        bingo = bingoCheck(bingoNumbers[i])
        if bingo == True:
            return

    print("Bingo not found!")


bingoLoop()
