input = open("input.txt", "r")

crabs = input.readline().split(',')
crabs = [int(i) for i in crabs]
crabs.sort()

# Part 1
med = crabs[len(crabs)//2]
print(sum(abs(crab - med) for crab in crabs))

# Part 2
mean = int(sum(crabs)/len(crabs))
print(sum((n := abs(mean - crab)) * (n+1)//2 for crab in crabs))
