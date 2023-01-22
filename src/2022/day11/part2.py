import copy
from functools import reduce

file = open('src/2022/day11/input.txt', 'r')
lines = file.readlines()

# parse Monkey input
monkeys = []
currMonkey = None
for line in lines:
  line = line.strip()
  if line.startswith('Monkey'):
    currMonkey = { "name": str(line[7]), "inspections": 0 }
  if line.startswith('Starting items:'):
    currMonkey["items"] = [int(x) for x in line.split(': ')[1].split(',')]
  if line.startswith('Operation:'):
    currMonkey["operation"] = line.split('= ')[1].split(' ')[1][0]
    operand0Str = line.split('= ')[1].split(' ')[0]
    currMonkey["operand0"] = 'old' if operand0Str == 'old' else int(operand0Str)
    operand1Str = line.split('= ')[1].split(' ')[2]
    currMonkey["operand1"] = 'old' if operand1Str == 'old' else int(operand1Str)
  if line.startswith('Test:'):
    currMonkey["divisibleByTest"] = int(line.split('divisible by ')[1])
  if line.startswith('If true:'):
    currMonkey["ifTrue"] = line.split('throw to monkey ')[1]
  if line.startswith('If false:'):
    currMonkey["ifFalse"] = line.split('throw to monkey ')[1]
    monkeys.append(copy.deepcopy(currMonkey))

divisibleByList = list(map(lambda monkey: monkey["divisibleByTest"], monkeys))
modulo = reduce((lambda x, y: x * y), divisibleByList)

for round in range(0, 10000):
  for monkey in monkeys:
    while len(monkey['items']) != 0:
      monkey["inspections"] += 1
      itemWorry = monkey['items'][0]
      operand0 = itemWorry if monkey["operand0"] == 'old' else monkey["operand0"]
      operand1 = itemWorry if monkey["operand1"] == 'old' else monkey["operand1"]
      if monkey["operation"] == '+':
        newItemWorry = (operand0 + operand1) % modulo
      else:
        newItemWorry = (operand0 * operand1) % modulo
      if newItemWorry % monkey["divisibleByTest"] == 0:
        passToMonkey = list(filter(lambda possibleMonkey: possibleMonkey["name"] == monkey["ifTrue"], monkeys))[0]
      else:
        passToMonkey = list(filter(lambda possibleMonkey: possibleMonkey["name"] == monkey["ifFalse"], monkeys))[0]
      
      passToMonkey["items"].append(newItemWorry)
      monkey['items'].pop(0)

monkeys.sort(key=lambda monkey: monkey['inspections'], reverse=True)

print(monkeys[0]['inspections'] * monkeys[1]['inspections'])