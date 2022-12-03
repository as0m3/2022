input = open("input.txt", "r")

count = 0


def contains(string: str, set):
    for char in set:
        if char not in string:
            return False
    return True


for line in input:
    line = line.split(" | ")
    line[1] = line[1].strip()
    outputValues = line[1].split(" ")
    num = ""
    for output in outputValues:
        if len(output) == 2:
            num += "1"
        elif len(output) == 3:
            num += "7"
        elif len(output) == 4:
            num += "4"
        elif len(output) == 5:
            # 2, 3, 5
            one = [i for i in outputValues if len(i) == 2]
            eight = [i for i in outputValues if len(i) == 7]
            if contains(output, list(one)) == True:
                num += "3"
            elif contains(eight, list(output)) == True:
                num += "-"
            else:
                num += "2"

        elif len(output) == 6:
            # 0, 6, 9
            # one = [i for i in outputValues if len(i) == 2]
            # four = [i for i in outputValues if len(i) == 4]
            num += "+"

        elif len(output) == 7:
            num += "8"
    # count += int(num)
    # print(num)
with open('input.txt') as f:
    lines = f.read().splitlines()

signals = []
outputs = []
r1 = 0
for line in lines:
    line = line.split(' | ')
    signals.append(line[0].split())
    outputs.append(line[1].split())
    r1 += sum([(2 <= len(i) <= 4) or len(i) == 7 for i in outputs[-1]])

print(r1)

r2 = 0
for signal, output in zip(signals, outputs):
    mapping = ['' for i in range(10)]
    signal = sorted(signal, key=len)
    for i in signal:
        if len(i) == 2:
            mapping[1] = i
        elif len(i) == 3:
            mapping[7] = i
        elif len(i) == 4:
            mapping[4] = i
        elif len(i) == 5:
            if all([c in i for c in mapping[1]]):
                mapping[3] = i
            elif sum([c in i for c in mapping[4]]) == 3:
                mapping[5] = i
            else:
                mapping[2] = i
        elif len(i) == 6:
            if all([c in i for c in mapping[4]]):
                mapping[9] = i
            elif all([c in i for c in mapping[7]]):
                mapping[0] = i
            else:
                mapping[6] = i
        else:
            mapping[8] = i

    output_number = 0
    for j, n in enumerate(output[::-1]):
        for i in range(10):
            if all([c in n for c in mapping[i]]) and len(mapping[i]) == len(n):
                output_number += i * 10 ** j
                break

    r2 += int(output_number)

print(r2)

#print("Count: ", count)
