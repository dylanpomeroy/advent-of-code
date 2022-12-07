file = open('src/2022/day6/sample.txt', 'r')
lines = file.readlines()
input = lines[0]

char0 = input[0]
char1 = input[1]
char2 = input[2]
result = 4
for index in range(3, len(input)):
  if char0 not in [char1, char2, input[index]] \
    and char1 not in [char0, char2, input[index]] \
    and char2 not in [char0, char1, input[index]] \
    and input[index] not in [char0, char1, char2]:
      break
  result += 1
  char0 = char1
  char1 = char2
  char2 = input[index]

print('Result: ', result)