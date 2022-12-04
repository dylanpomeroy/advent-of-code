file = open('input.txt', 'r')
lines = file.readlines()

# ord('a') - 96 = 1
# ord('A') - 38 = 27



total = 0
for rucksack in lines:
    firstHalf = rucksack[:len(rucksack) // 2]
    secondHalf = rucksack[len(rucksack) // 2:]

    firstHalfMap = {firstHalf[i]: 1 for i in range(0, len(firstHalf), 2)}
    inBoth = 'a'
    for char in secondHalf:
        if char in firstHalf:
            inBoth = char
            break

    priority = ord(char) - 96 if char.islower() else ord(char) - 38
    total += priority


print('Total: ', total)
