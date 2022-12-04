file = open('input.txt', 'r')
lines = file.readlines()

pairsWithEncoumpass = 0
for pair in lines:
    first = pair.split(',')[0]
    second = pair.split(',')[1]

    firstStart = int(first.split('-')[0])
    firstEnd = int(first.split('-')[1])
    secondStart = int(second.split('-')[0])
    secondEnd = int(second.split('-')[1])

    if (firstStart <= secondStart and firstEnd >= secondStart) or \
        (firstStart <= secondEnd and firstEnd >= secondEnd) or \
        (secondStart <= firstStart and secondStart >= firstStart) or \
        (secondStart <= firstEnd and secondEnd >= firstEnd):
        pairsWithEncoumpass += 1

print('Result: ', pairsWithEncoumpass)
