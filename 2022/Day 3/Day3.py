file = open("2022\Day 3\input.txt", 'r')


def main():
    total_prio = 0
    for line in file:
        middle_index: int = (len(line))//2
        first_half = line[:middle_index]
        second_half = line[middle_index:].strip()
        s = set(first_half) & set(second_half)
        ascii = int(ord(str(s).strip("{''}")))
        if ascii >= 97:
            total_prio += (ascii - 96)
        else:
            total_prio += (ascii - 38)
    file.close()
    print("Total Prio: ", total_prio)


if __name__ == "__main__":
    main()
