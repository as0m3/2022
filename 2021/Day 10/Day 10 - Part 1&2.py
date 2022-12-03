input = open("input.txt", "r")

chunks = {"(": ")", "[": "]", "{": "}", "<": ">"}
errors = {")": 3, "]": 57, "}": 1197, ">": 25137}
points = {")": 1, "]": 2, "}": 3, ">": 4}

errorScore = 0

list = []
corruptList = []

for line in input:
    line = line.strip()
    list.append(line)
    stack = []
    for char in line:
        if char in ("(", "[", "{", "<"):
            stack.append(char)
        else:
            check = stack.pop()
            if chunks[check] != char:
                errorScore += errors[char]
                corruptList.append(line)
                break
    stack.clear()

# Part 2
# New list containing only incomplete lines
new_list = [line for line in list if line not in corruptList]

scores = []

for line in new_list:
    stack = []
    for char in line:
        if char in ("(", "[", "{", "<"):
            stack.append(char)
        else:
            check = stack.pop()
    pointScore = 0
    for i in range(len(stack)-1, -1, -1):
        pointScore *= 5
        pointScore += points[chunks[stack[i]]]
    scores.append(pointScore)
    stack.clear()

scores.sort()
middleScore = scores[int((len(scores)-1)/2)]

print("Error Score:", errorScore)  # Part 1
print("Middle Score:", middleScore)  # Part 2
