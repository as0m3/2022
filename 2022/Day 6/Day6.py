file = open("Day 6\input.txt", 'r')
input = file.read()
file.close()


def main():
    for i in range(len(input)):
        s = {input[i], input[i+1], input[i+2], input[i+3]}
        if len(s) == 4:
            print(i+4)
            break
        del(s)


if __name__ == "__main__":
    main()
