file = open('src/2022/day9/input.txt', 'r')
lines = file.readlines()

placesTailHasBeen = set()
head = [0,0]
tail = [0,0]

insCount = 0
distCount = 0
for instruction in lines:
  insCount += 1
  direction = instruction.split(' ')[0]
  distance = int(instruction.split(' ')[1])
  
  for i in range(0, distance):
    distCount += 1
    if direction == 'R':
      head = [head[0] + 1, head[1]]
    elif direction == 'U':
      head = [head[0], head[1] - 1]
    elif direction == 'D':
      head = [head[0], head[1] + 1]
    elif direction == 'L':
      head = [head[0] - 1, head[1]]
    
    xAway = head[0] - tail[0]
    towardsX = 1 if xAway > 0 else -1
    yAway = head[1] - tail[1]
    towardsY = 1 if yAway > 0 else -1
    
    if abs(xAway) == 2 and yAway == 0:
      tail = [tail[0] + towardsX, tail[1]]
    elif xAway == 0 and abs(yAway) == 2:
      tail = [tail[0], tail[1] + towardsY]
    elif (abs(xAway) == 2 and abs(yAway) == 1) or (abs(xAway) == 1 and abs(yAway) == 2):
      tail = [tail[0] + towardsX, tail[1] + towardsY]
    
    placesTailHasBeen.add(str(tail[0]) + ',' + str(tail[1]))
    
print(len(placesTailHasBeen))
      
