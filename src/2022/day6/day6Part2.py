input = ''

result = 14
for index in range(0, len(input)):
  lastCharSet = set(input[index:(index+14)])
  if len(lastCharSet) == 14:
    break
  result += 1

print('Result: ', result)