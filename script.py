# Jacky Teoh
# GRAPH-SEARCH Algorithm with A* Search strategy for the 8-puzzle problem
import random
import heapq
import copy

global goal
goal = [[1, 2, 3], 
		[4, 5, 6], 
		[7, 8, 0]]

positions_of_goal = {1: (0, 0),
					 2: (0, 1),
					 3: (0, 2),
					 4: (1, 0),
					 5: (1, 1),
					 6: (1, 2),
					 7: (2, 0),
					 8: (2, 1),
					 0: (2, 2)}

curr_positions = {}

all_manhattan_distances = {1: float('inf'),
						   2: float('inf'),
						   3: float('inf'),
						   4: float('inf'),
						   5: float('inf'),
						   6: float('inf'),
						   7: float('inf'),
						   8: float('inf'),
						   0: float('inf')}

global initial_manhattan_sum
global pqueue
#global visited
initial_manhattan_sum = 0
grid = None
#visited = set()
number_of_nodes_generated = 0
pqueue = []

def find_manhattan_distance(x1, y1, x2, y2):
	manhattan_distance = abs(x1 - x2) + abs(y1 - y2)
	#all_manhattan_distances[grid[x1][y1]] = min(manhattan_distance, all_manhattan_distances[grid[x1][y1]])
	return manhattan_distance

def get_manhattan_sum(grid):
	manhattan_sum = 0
	for i in range(3):
		for j in range(3):
			value = grid[i][j]
			goal_x, goal_y = positions_of_goal[value][0], positions_of_goal[value][1]
			manhattan_sum += find_manhattan_distance(i, j, goal_x, goal_y)
	return manhattan_sum
'''	for key in curr_positions:
		curr_x, curr_y = curr_positions[key][0], curr_positions[key][1]
		goal_x, goal_y = positions_of_goal[key][0], positions_of_goal[key][1]

		curr_distance = find_manhattan_distance(curr_x, curr_y, goal_x, goal_y)
		all_manhattan_distances[grid[curr_x][curr_y]] = curr_distance
		manhattan_sum += curr_distance

	return manhattan_sum'''

def generate_random_board():
	# Create a randomized 3x3 matrix
	grid = [[0]*3 for _ in range(3)]
	possible_numbers = set(num for num in range(0, 9))

	# Populating the matrix:
	for i in range(3):
		for j in range(3):
			chosen = random.choice(list(possible_numbers))
			grid[i][j] = chosen
			curr_positions[chosen] = (i, j)
			possible_numbers.remove(chosen)

	global initial_manhattan_sum
	initial_manhattan_sum = get_manhattan_sum(grid)

	return grid

def tuplify(grid):
	return [tuple(arr) for arr in grid]

def listify(tuple):
	return [list(arr) for arr in tuple]

def find_position_of_zero(grid):
	#return curr_positions[0]
	for i in range(3):
		for j in range(3):
			if grid[i][j] == 0:
				return (i, j)
# Move left INTO the zero position, Zero must NOT have a y value of 2
# Number of nodes generated before calling move_left?
def move_left(input_grid, old_manhattan_sum, seen, path):
	#print("input", input_grid)
	#print("entered move left")
	zero_location_x, zero_location_y = find_position_of_zero(input_grid)
	to_move_x, to_move_y = zero_location_x, zero_location_y + 1
	new_grid = [arr[:] for arr in input_grid]
	new_seen = copy.deepcopy(seen)
	#print("new after left", new_grid)
	#print("new_grid before left swap", new_grid)
	#print(input_grid)
	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]
	#print("new_grid after left swap", new_grid)
	#print(input_grid)
	#input_grid[zero_location_x][zero_location_y], input_grid[to_move_x][to_move_y] = input_grid[to_move_x][to_move_y], input_grid[zero_location_x][zero_location_y]
	#print("new after left", new_grid)
	new_manhattan_sum = get_manhattan_sum(new_grid)
	#print("old manhattan_sum", old_manhattan_sum)
	#print("new manhattan sum", new_manhattan_sum)
	if new_manhattan_sum < old_manhattan_sum:
		#print("less")
		global pqueue
		#global visited
		global number_of_nodes_generated
		formatted = tuple(tuplify(new_grid))
		if formatted not in new_seen:
			new_seen.add(formatted)
			heapq.heappush(pqueue, (new_manhattan_sum, new_grid, new_seen, path + ["Left"]))
			#print("after left", pqueue)
			number_of_nodes_generated += 1
	#else:
	#	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]

def move_right(input_grid, old_manhattan_sum, seen, path):
	#print("input", input_grid)
	#print("entered move left")
	zero_location_x, zero_location_y = find_position_of_zero(input_grid)
	to_move_x, to_move_y = zero_location_x, zero_location_y - 1
	new_grid = [arr[:]for arr in input_grid]
	new_seen = copy.deepcopy(seen)
	#print("new after left", new_grid)
	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]
	#input_grid[zero_location_x][zero_location_y], input_grid[to_move_x][to_move_y] = input_grid[to_move_x][to_move_y], input_grid[zero_location_x][zero_location_y]
	#print("new after left", new_grid)
	new_manhattan_sum = get_manhattan_sum(new_grid)
	#print("old manhattan_sum", old_manhattan_sum)
	#print("new manhattan sum", new_manhattan_sum)
	if new_manhattan_sum < old_manhattan_sum:
		#print("less")
		global pqueue
		#global visited
		global number_of_nodes_generated
		formatted = tuple(tuplify(new_grid))
		if formatted not in new_seen:
			new_seen.add(formatted)
			heapq.heappush(pqueue, (new_manhattan_sum, new_grid, new_seen, path + ["Right"]))
			#print("after left", pqueue)
			number_of_nodes_generated += 1
	#else:
	#	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]

def move_up(input_grid, old_manhattan_sum, seen, path):
	#print("input", input_grid)
	#print("entered move left")
	zero_location_x, zero_location_y = find_position_of_zero(input_grid)
	to_move_x, to_move_y = zero_location_x + 1, zero_location_y
	new_grid = [arr[:] for arr in input_grid]
	new_seen = copy.deepcopy(seen)
	#print("new after left", new_grid)
	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]
	#input_grid[zero_location_x][zero_location_y], input_grid[to_move_x][to_move_y] = input_grid[to_move_x][to_move_y], input_grid[zero_location_x][zero_location_y]
	#print("new after left", new_grid)
	new_manhattan_sum = get_manhattan_sum(new_grid)
	#print("old manhattan_sum", old_manhattan_sum)
	#print("new manhattan sum", new_manhattan_sum)
	if new_manhattan_sum < old_manhattan_sum:
		#print("less")
		global pqueue
		#global visited
		global number_of_nodes_generated
		formatted = tuple(tuplify(new_grid))
		if formatted not in new_seen:
			new_seen.add(formatted)
			heapq.heappush(pqueue, (new_manhattan_sum, new_grid, new_seen, path + ["Up"]))
			#print("after left", pqueue)
			number_of_nodes_generated += 1
	#else:
	#	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]

def move_down(input_grid, old_manhattan_sum, seen, path):
	#print("input", input_grid)
	#print("entered move left")
	zero_location_x, zero_location_y = find_position_of_zero(input_grid)
	to_move_x, to_move_y = zero_location_x - 1, zero_location_y
	new_grid = [arr[:] for arr in input_grid]
	new_seen = copy.deepcopy(seen)
	#print("new after left", new_grid)
	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]
	#input_grid[zero_location_x][zero_location_y], input_grid[to_move_x][to_move_y] = input_grid[to_move_x][to_move_y], input_grid[zero_location_x][zero_location_y]
	#print("new after left", new_grid)
	new_manhattan_sum = get_manhattan_sum(new_grid)
	#print("old manhattan_sum", old_manhattan_sum)
	#print("new manhattan sum", new_manhattan_sum)
	if new_manhattan_sum < old_manhattan_sum:
		#print("less")
		global pqueue
		#global visited
		global number_of_nodes_generated
		formatted = tuple(tuplify(new_grid))
		if formatted not in new_seen:
			new_seen.add(formatted)
			heapq.heappush(pqueue, (new_manhattan_sum, new_grid, new_seen, path + ["Down"]))
			#print("after left", pqueue)
			number_of_nodes_generated += 1
	#else:
	#	new_grid[zero_location_x][zero_location_y], new_grid[to_move_x][to_move_y] = new_grid[to_move_x][to_move_y], new_grid[zero_location_x][zero_location_y]

#grid = generate_random_board()
#print(grid)
#print(curr_positions)
#print(find_position_of_zero(grid))
#tupled = tuple(tuplify(grid))
#visited.add(tupled)
'''test = [[1, 2, 3], 
		[4, 5, 6], 
		[7, 0, 8]]

print(test)
test_sum = get_manhattan_sum(test)
print(test_sum)
print(pqueue)
move_left(test, test_sum)
print(pqueue)
print(visited)'''

def solve():
	global pqueue
	global initial_manhattan_sum
	global visited
	global goal

	grid = generate_random_board()
	#print(grid)
	#grid = [[1, 2, 3], 
	#		[4, 5, 6], 
	#		[0, 7, 8]]
	#first = find_position_of_zero(grid)
	#initial_manhattan_sum = get_manhattan_sum(grid)

	initial_seen = set()
	initial_seen.add(tuple(tuplify(grid)))

	heapq.heappush(pqueue, (initial_manhattan_sum, grid, initial_seen, []))
	#visited.add(tuple(tuplify(grid)))
	#print(pqueue)
	while pqueue:
		#print(pqueue)
		#print("Visited:")
		#for board in visited:
		#	for line in board:
		#		print(line)
		#	print(",")
		popped_sum, popped_grid, popped_visited, popped_path = heapq.heappop(pqueue)
		#popped_visited.add(tuple(tuplify(popped_grid)))
		#print (popped_sum, popped_grid, popped_visited, popped_path)
		#print(popped_grid)
		#print(tuple(tuplify(popped_grid)))
		#print(popped_grid)
		#print(goal)
		#copied = [arr for arr in popped_grid]
		#print(copied)
		if popped_grid == goal:
			print ("Hey we did it!")
			#print(visited)
			#print(popped_visited)
			print(number_of_nodes_generated)
			print(popped_path)
			return
		zero = find_position_of_zero(popped_grid)
		print("Sum:", popped_sum, "Popped:", popped_grid, "Path:", popped_path)
		# Left
		if zero[1] != 2:
			#copied = [arr for arr in popped_grid]
			#print(popped_grid, "vs", copied)
			#print(copied)
			#print("Go left")
			#move_left(popped_grid, popped_sum, popped_path)
			#print("before left:", popped_visited)
			move_left(popped_grid, popped_sum, popped_visited, popped_path)
			#print("after left:", popped_visited)
			#print("Pqueue after left:", pqueue)
		# Right
		if zero[1] != 0:
			#copied = [arr for arr in popped_grid]
			#print("Go right")
			#print("Popped grid @ Right", popped_grid)
			move_right(popped_grid, popped_sum, popped_visited, popped_path)
			#print(pqueue)
		# Up
		if zero[0] != 2:
			#copied = [arr for arr in popped_grid]
			#print("Go up")
			move_up(popped_grid, popped_sum, popped_visited, popped_path)
			#print(pqueue)
		# Down
		if zero[0] != 0:
			#print("Popped:", popped_grid)
			#copied = [arr for arr in popped_grid]
			#print(popped_grid, "vs", copied)
			#print("Go down")
			move_down(popped_grid, popped_sum, popped_visited, popped_path)
			#print(pqueue)
		#print("end of while", popped_visited)
		print(pqueue)
		#print("Next iteration")
	print("Answer not found?")

solve()


#print(visited) {((2, 4, 5), (0, 6, 8), (3, 1, 7))}
#print(listify(tupled)) [[2, 4, 5], [0, 6, 8], [3, 1, 7]]

'''if tuple(tupled) in visited:
	print("True")
next_rand = generate_random_board()
tupled_rand = [tuple(arr) for arr in next_rand]
visited.add(tuple(tupled_rand))
print(visited)
visited.add(tuple(tupled_rand))
print(visited)'''

#heapq.heappush(pqueue, _, move?)

'''
# Move left, right, up, down
# This move will be the move INTO the 0 position. 
def move_left(x, y, board, path, manhattan_sum):
	if y == 2:
		return
	else:
		dist_of_new_zero = find_manhattan_distance(x, y - 1, )
		#manhattan distance total? if lower than current then append to pqueue?
		# curr, to_move = board[x][y], board[x][y + 1]
		# curr, to_move = to_move, curr
		board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
		#if manhattan_dist < curr_dist: pqueue.append(x, y + 1, board, path + "Left", min(manhattan_sum, curr_sum))
		#update curr_positions?

		#Maybe just subtract the distances of the ones to be moved, and then readd the new positions distances
		# to the sum and see if higher/lower?
		
		#pqueue = []
        #end = 11
        #heappush(pqueue, (10, "Steak"))
        #heappush(pqueue, (3, "Chicken"))
        #heappush(pqueue, (2, "Fish"))
        #print(pqueue)
        #while end:
        #    #print(pqueue)
        #    print(heappushpop(pqueue, (end, "Steak")))
        #    end -= 1
		
def move_right(x, y, board, path):

def move_up(x, y, board, path):

def move_down(x, y, board, path):
'''