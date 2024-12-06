

def main():
    file = open("Day 1\input.txt", 'r')
    left: int = []
    right: int = []
    for line in file:
        line = line.strip()
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))

    left.sort()
    right.sort()
    
    # Part A
    answer: int = 0
    for i in range(len(left)):
        answer += abs(left[i] - right[i])

    print('A:', answer)

    # Part B
    similarity: int = 0
    for i in range(len(left)):
        similarity += (left[i] * right.count(left[i]))
    
    print('B:', similarity)

    file.close()
if __name__ == '__main__':
    main()

