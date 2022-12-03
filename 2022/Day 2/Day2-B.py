# Them               ME
# A =     Rock      = [+1]X (Lose)[+0]
# B =    Paper      = [+2]Y (Draw)[+3]
# C =   Scissors    = [+3]Z (Win)[+6]

import string


def main():
    file = open("Day 2\input.txt", 'r')

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
            if them == 'A':
                total_score += 3
            if them == 'B':
                total_score += 1
            if them == 'C':
                total_score += 2
        if me == 'Y':
            total_score += 3
            if them == 'A':
                total_score += 1
            if them == 'B':
                total_score += 2
            if them == 'C':
                total_score += 3
        if me == 'Z':
            total_score += 6
            if them == 'A':
                total_score += 2
            if them == 'B':
                total_score += 3
            if them == 'C':
                total_score += 1

    file.close()
    print("Total Score: ", total_score)


if __name__ == '__main__':
    main()
