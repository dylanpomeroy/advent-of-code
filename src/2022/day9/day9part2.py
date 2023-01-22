file = open('src/2022/day9/input.txt', 'r')
lines = file.readlines()

placesTailHasBeen = set()
head = [0,0]
tails = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]

def printBoard(height, width):
  board = [['.']*width for _ in range(height)]
  for index, tail in enumerate(reversed(tails)):
    board[len(board) + tail[1] - 1][tail[0]] = str(len(tails) - index)
  
  board[len(board) + head[1] - 1][head[0]] = 'H'
  
  for row in board:
    print(' '.join(row))
  print()

boardHeight = 5
boardWidth = 6

insCount = 0
distCount = 0
iteration = 1
for instruction in lines:
  insCount += 1
  direction = instruction.split(' ')[0]
  distance = int(instruction.split(' ')[1])
  
  for _ in range(0, distance):
    distCount += 1
    if direction == 'R':
      head = [head[0] + 1, head[1]]
    elif direction == 'U':
      head = [head[0], head[1] - 1]
    elif direction == 'D':
      head = [head[0], head[1] + 1]
    elif direction == 'L':
      head = [head[0] - 1, head[1]]
    
    for tailIndex in range(0, len(tails)):
      relativeHead = head if tailIndex == 0 else tails[tailIndex-1]
      
      xAway = relativeHead[0] - tails[tailIndex][0]
      towardsX = 1 if xAway > 0 else -1
      yAway = relativeHead[1] - tails[tailIndex][1]
      towardsY = 1 if yAway > 0 else -1
      
      if abs(xAway) == 2 and abs(yAway) == 2:
        tails[tailIndex] = [tails[tailIndex][0] + towardsX, tails[tailIndex][1] + towardsY]
      elif abs(xAway) == 2 and yAway == 0:
        tails[tailIndex] = [tails[tailIndex][0] + towardsX, tails[tailIndex][1]]
      elif xAway == 0 and abs(yAway) == 2:
        tails[tailIndex] = [tails[tailIndex][0], tails[tailIndex][1] + towardsY]
      elif (abs(xAway) == 2 and abs(yAway) == 1) or (abs(xAway) == 1 and abs(yAway) == 2):
        tails[tailIndex] = [tails[tailIndex][0] + towardsX, tails[tailIndex][1] + towardsY]
    
    placesTailHasBeen.add(str(tails[8][0]) + ',' + str(tails[8][1]))
    #print('Iteration: ', str(iteration))
    #printBoard(boardHeight, boardWidth)
    iteration += 1
    
    
print(len(placesTailHasBeen))
      
