
file = open("2022\Day 4\input.txt", 'r')


def main():
    total_full_overlaps = 0
    total_partial_overlaps = 0
    for line in file:
        pair = line.strip().split(',')
        pair[0] = pair[0].split('-')
        pair[1] = pair[1].split('-')
        x1 = int(pair[0][0])
        y1 = int(pair[0][1])
        x2 = int(pair[1][0])
        y2 = int(pair[1][1])
        if(((x1 <= x2) and (y1 >= y2)) or ((x2 <= x1) and (y2 >= y1))):
            total_full_overlaps += 1

        if(((x1 >= x2) and (x1 <= y2)) or ((x2 >= x1) and (x2 <= y1))):
            total_partial_overlaps += 1
            continue
        elif(((y1 >= x2) and (y1 <= y2)) or ((y2 >= x1) and (y2 <= y1))):
            total_partial_overlaps += 1
            continue
        else:
            continue

    file.close()
    print("Full Overlaps: ", total_full_overlaps,
          "\nPartial Overlaps: ", total_partial_overlaps)


if __name__ == "__main__":
    main()
