elfTotals = []

file = open("input.txt", "r")
lines = file.readlines()

elfCalories = int(lines[0])
for line in lines[1:]:
    if line == '\n':
        elfTotals.append(elfCalories)
        elfCalories = 0
    else:
        elfCalories += int(line)

print(elfTotals)

first = max(elfTotals)
elfTotals.remove(first)
second = max(elfTotals)
elfTotals.remove(second)
third = max(elfTotals)
elfTotals.remove(third)

print('Total max: ', first + second + third)

