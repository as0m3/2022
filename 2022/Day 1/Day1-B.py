def main():
    file = open("2022\Day 1\input.txt", 'r')

    sum: int = 0
    sums: int = []
    for line in file:
        line.strip()
        if line == '\n':
            sums.append(sum)
            sum = 0
            continue
        sum += int(line)

    file.close()
    # reverse=True descending order so top 3 are first 3 elements of sum list
    sums.sort(reverse=True)
    print("Sum of top 3 Calories: ", (sums[0] + sums[1] + sums[2]))


if __name__ == '__main__':
    main()
