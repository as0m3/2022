file = open("Day 5\input.txt", 'r')

s1 = ['W', 'R', 'F']
s2 = ['T', 'H', 'M', 'C', 'D', 'V', 'W', 'P']
s3 = ['P', 'M', 'Z', 'N', 'L']
s4 = ['J', 'C', 'H', 'R']
s5 = ['C', 'P', 'G', 'H', 'Q', 'T', 'B']
s6 = ['G', 'C', 'W', 'L', 'F', 'Z']
s7 = ['W', 'V', 'L', 'Q', 'Z', 'J', 'G', 'C']
s8 = ['P', 'N', 'R', 'F', 'W', 'T', 'V', 'C']
s9 = ['J', 'W', 'H', 'G', 'R', 'S', 'V']

stacks = [s1, s2, s3, s4, s5, s6, s7, s8, s9]


def main():
    for line in file:
        line = line.replace("move", '').replace("from", '').replace("to", '')
        line = line.strip().split()
        move((int(line[0])), int(line[1]), int(line[2]))
    file.close()
    answer = ""
    for stack in stacks:
        answer += stack[-1]
    print("Answer: ", answer)


def move(amount: int, _from: int, to: int):
    for _ in range(amount):
        stacks[to-1].append(stacks[_from-1].pop())


if __name__ == "__main__":
    main()
