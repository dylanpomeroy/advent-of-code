file = open('src/2022/day7/sample.txt', 'r')
lines = file.readlines()

currDir = ''
fileTree = {
  "name": "/",
  "dirs": [],
  "files": [],
  "parent": None,
}

currentTreeNode = fileTree
for line in lines:
  if line.startswith('$'):
    command = line[2:].split(' ')[0]
    if command == 'cd':
      cdInput = line[4:].strip()
      if cdInput == '/':
        currDir = ''
        currentTreeNode = fileTree
      elif cdInput == '..':
        currDir = currDir[:currDir.rindex('/')]
        currentTreeNode = currentTreeNode["parent"]
      else:
        currDir += '/' + cdInput
        if cdInput not in currentTreeNode:
          currentTreeNode["dirs"].append({ "name": cdInput, "dirs": [], "files": [], "parent": currentTreeNode})
        currentTreeNode = list(filter(lambda x: x["name"] == cdInput, currentTreeNode["dirs"]))[0]
  elif line.startswith('dir '):
    continue
  else:
    # reading ls line
    fileSize = int(line.split(' ')[0].strip())
    fileName = line.split(' ')[1].strip()
    if any(x["name"] == fileName for x in currentTreeNode["files"]):
      continue
    else:
      currentTreeNode["files"].append({ "name": fileName, "size": fileSize })


totalSizeOfLargeDirs = 0
largeDirNames = []
def getDirSize(currentTreeNode):
  global totalSizeOfLargeDirs
  global largeDirNames
  size = 0
  for file in currentTreeNode["files"]:
    size += file["size"]
  
  for dir in currentTreeNode["dirs"]:
    size += getDirSize(dir)
  
  if currentTreeNode["name"] != '/' and size <= 100000:
    totalSizeOfLargeDirs += size
    largeDirNames.append(currentTreeNode["name"])
    
  currentTreeNode["size"] = size
  return size

getDirSize(fileTree)

print(totalSizeOfLargeDirs)
    
  
  
  