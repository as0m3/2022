file = open("input.txt", "r")
output = open("output2.txt", "w")

lines = []

diagram = []
for i in range(1000):
    row = []
    for j in range(1000):
        row.append(0)
    diagram.append(row)


def overlapCount():
    count = 0
    for i in range(1000):
        for j in range(1000):
            if int(diagram[i][j]) >= 2:
                count += 1
    return count


def printDiagram():
    for i in range(len(diagram)):
        out = ""
        for j in range(len(diagram[i])):
            out += str(diagram[i][j])
        out += "\n"
        output.write(out)


def writeCoord(x1: int, y1: int, x2: int, y2: int):
    xRange = x2-x1
    yRange = y2-y1
    if xRange != 0:
        if xRange > 0:
            for x in range(x1, x2+1):
                diagram[x][y1] += 1
        elif xRange < 0:
            for x in range(x2, x1+1):
                diagram[x][y1] += 1
        else:
            print("Should not happen! - 1")
            print(x1, y1, x2, y2)
    elif yRange != 0:
        if yRange > 0:
            for y in range(y1, y2+1):
                diagram[x1][y] += 1
        elif yRange < 0:
            for y in range(y2, y1+1):
                diagram[x1][y] += 1
        else:
            print("Should not happen! - 2")
            print(x1, y1, x2, y2)
    else:
        print("Should not happen! - 3")
        print(x1, y1, x2, y2)


def writeDiagCord(x1: int, y1: int, x2: int, y2: int):
    xRange = x2-x1
    yRange = y2-y1
    if x1 == y1 and x2 == y2:
        if xRange > 0:
            for i in range(x1, x2+1):
                diagram[i][i] += 1
        elif xRange < 0:
            for i in range(x2, x1+1):
                diagram[i][i] += 1
        else:
            print("Should not happen! - 4")
            print(x1, y1, x2, y2)
    elif x1-x2 == y2-y1:
        if yRange > 0:
            # -1 +1
            x = x1
            y = y1
            for i in range(yRange+1):
                diagram[x][y] += 1
                x -= 1
                y += 1
        elif yRange < 0:
            # +1 -1
            x = x1
            y = y1
            for i in range(xRange+1):
                diagram[x][y] += 1
                x += 1
                y -= 1
        else:
            print("Should not happen! - 5")
            print(x1, y1, x2, y2)
    elif x2-x1 == y2-y1:
        if xRange > 0:
            x = x1
            y = y1
            for i in range(y1, y2+1):
                diagram[x][y] += 1
                x += 1
                y += 1
        elif xRange < 0:
            x = x2
            y = y2
            for i in range(y2, y1+1):
                diagram[x][y] += 1
                x += 1
                y += 1
        else:
            print("Should not happen! - 6")
            print(x1, y1, x2, y2)
    else:
        print("Should not happen! - 7")
        print(x1, y1, x2, y2)


for line in file:
    lines.append(line.strip())

for i in range(len(lines)):
    lineSeg = lines[i].split(" -> ")
    left = lineSeg[0].split(",")
    right = lineSeg[1].split(",")
    x1 = int(left[0])
    y1 = int(left[1])
    x2 = int(right[0])
    y2 = int(right[1])
    if x1 == x2 or y1 == y2:
        writeCoord(x1, y1, x2, y2)
    elif (x1 == y1 and x2 == y2) or (x1-x2 == y2-y1) or (x2-x1 == y2-y1):
        writeDiagCord(x1, y1, x2, y2)
    else:
        print("Skipped: ", x1, y1, x2, y2)


printDiagram()
answer = overlapCount()
print("Count:", answer)

# END OF PROGRAM
file.close()
output.close()
