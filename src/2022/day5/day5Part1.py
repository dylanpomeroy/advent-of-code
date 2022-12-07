file = open('2022/day5/input.txt', 'r')
lines = file.readlines()

onStacks = True
stacks = [[], [], [], [], [], [], [], [], []]
for line in lines:
  if line.strip() == '':
    for stack in stacks:
      stack.reverse()
    onStacks = False
    continue
  
  for index in range(0, len(line), 4):
    if line[index] == ' ':
      continue
    if line[index] == '[':
      #if len(stacks) <= index // 4:
       #stacks.append([])
      stacks[index // 4].append(line[index+1])

  if not onStacks:
    numberToMove = int(line.split('move ')[1].split(' from')[0])
    moveFrom = int(line.split('from ')[1].split(' to')[0])-1
    moveTo = int(line.split('to ')[1].strip())-1

    boxes = []    
    for _ in range(0, numberToMove):
      boxes.append(stacks[moveFrom].pop())
    boxes.reverse() 
    stacks[moveTo].extend(boxes)
  
result = ''
for stack in stacks:
  if len(stack) == 0:
    continue
  result += stack.pop()
  
  


print('Result: ', result)