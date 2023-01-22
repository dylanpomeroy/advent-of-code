file = open('src/2022/day13/sample.txt', 'r')
lines = list(map(lambda x: x.strip(), file.readlines()))

def is_valid(a, b):
  return True    

packet_pairs = []
curr_pair = []
for line in lines:
  if line.strip() == '':
    packet_pairs.append(curr_pair)
    curr_pair = []
  else:
    curr_pair.append(line)

def trim_extra_brackets(part):
  if len(part) == 0: return part
  if part[0] == '[' and part[-1] != ']':
    return part[1:]
  if part[0] != '[' and part[-1] == ']':
    return part[0:-1]
  return part

def add_brackets(part):
  return '[' + part + ']'

def get_subparts(part):
  subparts = []
  curr_subpart = ''
  curr_nesting = 0
  for char in part[1:-1]:
    if char == '[':
      curr_nesting += 1
      curr_subpart += char
    elif char == ']':
      curr_nesting -= 1
      curr_subpart += char
    elif char == ',' and curr_nesting == 0:
      subparts.append(curr_subpart)
      curr_subpart = ''
    else:
      curr_subpart += char
  
  subparts.append(curr_subpart)
  return subparts

def is_valid_pair(a, b):
  a = trim_extra_brackets(a)
  b = trim_extra_brackets(b)
  
  if a == '' and b != '': return False
  if b == '': return True
  
  if a[0] != '[' and b[0] != '[':
    if int(a) == int(b): return None
    return int(a) < int(b)
  if a[0] == '[' and b[0] != '[':
    b = '[' + b + ']'
  elif a[0] != '[':
    a = '[' + b + ']'
  
  is_valid = True
  
  a_parts = get_subparts(a)
  b_parts = get_subparts(b)
  for index, a_part in enumerate(a_parts):
    if len(b_parts) == index:
      is_valid = False
      break
    curr_valid = is_valid_pair(a_part, b_parts[index])
    if curr_valid is None:
      continue
    if not curr_valid:
      is_valid = False
      break
  
  return is_valid

right_order_indices = []
for packet_pair_index, packet_pair in enumerate(packet_pairs):
  if is_valid_pair(packet_pair[0], packet_pair[1]):
    right_order_indices.append(packet_pair_index + 1)

print(sum(right_order_indices))
