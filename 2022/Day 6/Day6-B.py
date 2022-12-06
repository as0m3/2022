file = open("Day 6\input.txt", 'r')
input = file.read()
file.close()


def main():
    for i in range(len(input)):
        s = {input[i], input[i+1], input[i+2], input[i+3], input[i+4], input[i+5], input[i+6],
             input[i+7], input[i+8], input[i+9], input[i+10], input[i+11], input[i+12], input[i+13]}
        if len(s) == 14:
            print(i+14)
            break
        del(s)


if __name__ == "__main__":
    main()
