file = open('input.txt', 'r')
lines = file.readlines()

# 0 for loss
# 3 for tie
# 6 for win

# 1 for rock = A / X
# 2 for paper = B / Y
# 3 for scissors C / Z


playScores = {
    'A X': 0,
    'A Y': 3,
    'A Z': 6,
    'B X': 0,
    'B Y': 3,
    'B Z': 6,
    'C X': 0,
    'C Y': 3,
    'C Z': 6,
}

handScores = {
    'A X': 3,
    'A Y': 1,
    'A Z': 2,
    'B X': 1,
    'B Y': 2,
    'B Z': 3,
    'C X': 2,
    'C Y': 3,
    'C Z': 1,
}

totalScore = 0
for line in lines:
    first = line.split(' ')[0].strip()
    second = line.split(' ')[1].strip()

    playScore = playScores[line.strip()]
    handScore = handScores[line.strip()]
    totalScore += playScore + handScore

print(totalScore)

