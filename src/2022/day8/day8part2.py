file = open('src/2022/day8/input.txt', 'r')
treeGrid = list(map(lambda x: x.strip(), file.readlines()))

bestScenicScore = 0
for row in range(1, len(treeGrid)-1):
  for col in range(1, len(treeGrid[0])-1):
    tree = treeGrid[row][col]
    leftFrom = col - 1
    leftScore = 0
    while leftFrom >= 0:
      leftScore += 1
      if treeGrid[row][leftFrom] >= tree: break
      leftFrom -= 1
    
    rightFrom = col + 1
    rightScore = 0
    while rightFrom <= len(treeGrid[0])-1:
      rightScore += 1
      if treeGrid[row][rightFrom] >= tree: break
      rightFrom += 1
      
    upFrom = row - 1
    upScore = 0
    while upFrom >= 0:
      upScore += 1
      if treeGrid[upFrom][col] >= tree: break
      upFrom -= 1
    
    downFrom = row + 1
    downScore = 0
    while downFrom <= len(treeGrid)-1:
      downScore += 1
      if treeGrid[downFrom][col] >= tree: break
      downFrom += 1
    
    scenicScore = leftScore * rightScore * upScore * downScore
    bestScenicScore = max(bestScenicScore, scenicScore)
    
print(bestScenicScore)
