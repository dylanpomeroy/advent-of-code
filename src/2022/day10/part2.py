file = open('src/2022/day10/input.txt', 'r')
lines = file.readlines()

screen = ['.'] * 240

def printScreen():
  for lineStart in range(0, len(screen), len(screen) // 6):
    print(''.join(screen[lineStart:lineStart + (240//6)]))
  print()

printScreen()

maxCycles = 1000000

lineIndex = 0
cycleLineStartedOn = None
xRegister = 1
nextXRegister = 1
for cycle in range(1, maxCycles):
  xRegister = nextXRegister
  if lineIndex == len(lines):
    break
  
  line = lines[lineIndex].strip()
  if line == 'noop':
    lineIndex += 1
  elif line.startswith('addx'):
    if cycleLineStartedOn == cycle - 1:
      nextXRegister += int(line.split(' ')[1])
      lineIndex += 1
      cycleLineStartedOn = None
    elif cycleLineStartedOn == None:
      cycleLineStartedOn = cycle
  
  screenIndex = cycle - 1
  xRegisterOffset = xRegister + (cycle // 40 * 40)
  if xRegisterOffset - 1 <= screenIndex and screenIndex <= xRegisterOffset + 1:
    screen[screenIndex] = '#'
  printScreen()

