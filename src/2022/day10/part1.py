file = open('src/2022/day10/input.txt', 'r')
lines = file.readlines()

maxCycles = 1000000

lineIndex = 0
cycleLineStartedOn = None
xRegister = 1
signalStrengthTotal = 0
for cycle in range(1, maxCycles):
  if cycle == 20 or (cycle - 20) % 40 == 0:
    signalStrengthTotal += cycle * xRegister
  
  if lineIndex == len(lines):
    break
  
  line = lines[lineIndex].strip()
  if line == 'noop':
    lineIndex += 1
  elif line.startswith('addx'):
    if cycleLineStartedOn == cycle - 1:
      xRegister += int(line.split(' ')[1])
      lineIndex += 1
      cycleLineStartedOn = None
    elif cycleLineStartedOn == None:
      cycleLineStartedOn = cycle
      continue
    
print(signalStrengthTotal)