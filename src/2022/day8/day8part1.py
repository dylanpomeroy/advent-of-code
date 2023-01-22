file = open('src/2022/day8/input.txt', 'r')
treeGrid = list(map(lambda x: x.strip(), file.readlines()))

def isVisibleFromLeft(row, col):
  for leftOf in range(col-1, -1, -1):
    if treeGrid[row][col] <= treeGrid[row][leftOf]:
      return False
  return True

def isVisibleFromRight(row, col):
  for rightOf in range(col+1, len(treeGrid[0]), 1):
    if treeGrid[row][col] <= treeGrid[row][rightOf]:
      return False
  return True

def isVisibleFromTop(row, col):
  for upFrom in range(row-1, -1, -1):
    if treeGrid[row][col] <= treeGrid[upFrom][col]:
      return False
  return True

def isVisibleFromBottom(row, col):
  for downFrom in range(row+1, len(treeGrid), 1):
    if treeGrid[row][col] <= treeGrid[downFrom][col]:
      return False
  return True

visibleTrees = 0
for row in range(0, len(treeGrid)):
  for col in range(0, len(treeGrid[0])):
    if row == 0 or row == len(treeGrid)-1 or col == 0 or col == len(treeGrid)-1:
      visibleTrees += 1
      continue
    
    if isVisibleFromLeft(row, col) \
        or isVisibleFromRight(row, col) \
        or isVisibleFromTop(row, col) \
        or isVisibleFromBottom(row, col):
      visibleTrees += 1
      
print(visibleTrees)
