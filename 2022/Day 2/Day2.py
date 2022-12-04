# Them               ME
# A =     Rock      = X
# B =    Paper      = Y
# C =   Scissors    = Z

import string


def main():
    file = open("2022\Day 2\input.txt", 'r')

    lines: string = []
    for line in file:
        line.strip()
        lines.append(line.split(' '))
        lines[-1][-1] = lines[-1][-1].strip()  # remove /n's from each element

    total_score = 0
    for i in range(len(lines)):
        them = lines[i][0]
        me = lines[i][1]
        if me == 'X':
            total_score += 1
            if them == 'C':
                total_score += 6
            if them == 'A':
                total_score += 3
            continue
        if me == 'Y':
            total_score += 2
            if them == 'A':
                total_score += 6
            if them == 'B':
                total_score += 3
            continue
        if me == 'Z':
            total_score += 3
            if them == 'B':
                total_score += 6
            if them == 'C':
                total_score += 3
            continue
    file.close()
    print("Total Score: ", total_score)


if __name__ == '__main__':
    main()
