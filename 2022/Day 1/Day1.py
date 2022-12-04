def main():
    file = open("2022\Day 1\input.txt", 'r')

    max: int = 0
    sum: int = 0
    for line in file:
        line.strip()
        if line == '\n':
            if sum > max:
                max = sum
            sum = 0
            continue
        sum += int(line)

    print("Max Calories: ", max)


if __name__ == '__main__':
    main()
