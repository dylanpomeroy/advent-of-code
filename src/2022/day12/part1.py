import copy
import sys

file = open('src/2022/day12/input.txt', 'r')
map = list(map(lambda line: line.strip(), file.readlines()))

heights = { 'S': 0, 'E': 25 }
def height_of(y, x): return ord(map[y][x]) - 97 if map[y][x] not in ['S', 'E'] else heights[map[y][x]]

def height_dif(y0, x0, y1, x1): return height_of(y1, x1) - height_of(y0, x0)

def can_reach(y0, x0, y1, x1): return height_dif(y0, x0, y1, x1) <= 1

def str_crd(y, x): return str(y) + ',' + str(x)

start_x = 0; start_y = 0; end_x = 0; end_y = 0
for index, line in enumerate(map):
  if 'S' in line:
    start_y = index
    start_x = line.index('S')
  if 'E' in line:
    end_y = index
    end_x = line.index('E')

start_coord_str = str_crd(start_y, start_x)
end_coord_str = str_crd(end_y, end_x)

visited_costs = { start_coord_str: 0 }
visited_coords = {}
while True:
  min_cost = sys.maxsize
  min_cost_coords_str = None
  for key in visited_costs.keys():
    if key not in visited_coords and visited_costs[key] < min_cost:
      min_cost = visited_costs[key]
      min_cost_coords_str = key

  curr_y = int(min_cost_coords_str.split(',')[0])
  curr_x = int(min_cost_coords_str.split(',')[1])
  
  curr_cost = visited_costs[str_crd(curr_y, curr_x)]
  new_coord_strings = []
  if curr_y > 0 and can_reach(curr_y, curr_x, curr_y-1, curr_x):
    new_coord_strings.append(str_crd(curr_y-1, curr_x))
  if curr_y < len(map) - 1 and can_reach(curr_y, curr_x, curr_y+1, curr_x):
    new_coord_strings.append(str_crd(curr_y+1, curr_x))
  if curr_x > 0 and can_reach(curr_y, curr_x, curr_y, curr_x-1):
    new_coord_strings.append(str_crd(curr_y, curr_x-1))
  if curr_x < len(map[0]) - 1 and can_reach(curr_y, curr_x, curr_y, curr_x+1):
    new_coord_strings.append(str_crd(curr_y, curr_x+1))
  
  for new_coord_string in new_coord_strings:
    if new_coord_string in visited_coords: continue
    old_cost = visited_costs[new_coord_string] if new_coord_string in visited_costs else sys.maxsize
    visited_costs[new_coord_string] = curr_cost + 1 if old_cost > curr_cost + 1 else old_cost
  visited_coords[str_crd(curr_y, curr_x)] = True
  
  if end_coord_str in visited_costs:
    break

print(visited_costs[end_coord_str])
  