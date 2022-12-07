file = open('input.txt', 'r')
lines = file.readlines()

# ord('a') - 96 = 1
# ord('A') - 38 = 27



total = 0
for i in range(0, len(lines), 3):
    firstRucksack = lines[i].strip()
    secondRucksack = lines[i+1].strip()
    thirdRucksack = lines[i+2].strip()

    inBoth = 'a'
    for char in thirdRucksack:
        print('checking char: ', char)
        if char in firstRucksack:
            if char in secondRucksack:
                inBoth = char
                print('found it!')
                break

    priority = ord(char) - 96 if char.islower() else ord(char) - 38
    print('adding: ', priority, ' for char: ', inBoth)
    total += priority

print('Total: ', total)

