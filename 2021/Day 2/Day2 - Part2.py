# Day 2 (Part 2) 12/1/2021

directions = open("input.txt", "r")

horizontal, depth, aim = 0, 0, 0

for direction in directions:

    direction = direction.split(" ")

    if (direction[0] == "up"):
        aim -= int(direction[1].strip())

    elif (direction[0] == "down"):
        aim += int(direction[1].strip())

    elif (direction[0] == "forward"):
        horizontal += int(direction[1].strip())
        depth += (aim * int(direction[1].strip()))

    else:
        print("Invalid direction!")

result = horizontal * depth
print(result)
