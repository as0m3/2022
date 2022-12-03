# Day 2 12/1/2021

directions = open("input.txt", "r")

horizontal, depth = 0, 0

for direction in directions:

    direction = direction.split(" ")

    if (direction[0] == "up"):
        depth -= int(direction[1].strip())

    elif (direction[0] == "down"):
        depth += int(direction[1].strip())

    elif (direction[0] == "forward"):
        horizontal += int(direction[1].strip())

    else:
        print("Invalid direction!")

result = horizontal * depth
print(result)
