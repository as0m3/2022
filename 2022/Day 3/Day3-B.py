file = open("2022\Day 3\input.txt", 'r')


def main():
    total_prio = 0
    lines = []
    for line in file:
        lines.append(line.strip())
    file.close()
    for i in range(0, len(lines), 3):
        s = set(lines[i]) & set(lines[i+1]) & set(lines[i+2])
        ascii = int(ord(str(s).strip("{''}")))
        if ascii >= 97:
            total_prio += (ascii - 96)
        else:
            total_prio += (ascii - 38)
    print("Total Prio: ", total_prio)


if __name__ == "__main__":
    main()
