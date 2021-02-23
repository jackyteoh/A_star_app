# Jacky Teoh
# GRAPH-SEARCH Algorithm with A* Search strategy for the 8-puzzle problem
import random
import heapq

goal = [[1, 2, 3], 
		[4, 5, 6], 
		[7, 8, 0]]

positions_of_goal = {1: (0, 0),
					 2: (0, 1),
					 3: (0, 2),
					 4: (1, 0),
					 5: (1, 1),
					 6: (1, 2)
					 7: (2, 0),
					 8: (2, 1),
					 0: (2, 2)}

curr_positions = {}

def generate_random_board():
	# Create a randomized 3x3 matrix
	grid = [[0]*3 for _ in range(3)]
	possible_numbers = set(num for num in range(0, 9))

	# Populating the matrix:
	for i in range(3):
		for j in range(3):
			chosen = choice(list(possible_numbers))
			grid[i][j] = chosen
			curr_positions[chosen] = (i, j)
			possible_numbers.remove(chosen)

	return grid

# Move left, right, up, down
# This move will be the move INTO the 0 position. 
def move_left(x, y, board, path, manhattan_sum):
	if y == 2:
		return
	else:
		#manhattan distance total? if lower than current then append to pqueue?
		# curr, to_move = board[x][y], board[x][y + 1]
		# curr, to_move = to_move, curr
		board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
		#if manhattan_dist < curr_dist: pqueue.append(x, y + 1, board, path + "Left", min(manhattan_sum, curr_sum))
		#update curr_positions?

		#Maybe just subtract the distances of the ones to be moved, and then readd the new positions distances
		# to the sum and see if higher/lower?
		'''
		pqueue = []
        end = 11
        heappush(pqueue, (10, "Steak"))
        heappush(pqueue, (3, "Chicken"))
        heappush(pqueue, (2, "Fish"))
        print(pqueue)
        while end:
            #print(pqueue)
            print(heappushpop(pqueue, (end, "Steak")))
            end -= 1
		'''


def move_right(x, y, board, path):

def move_up(x, y, board, path):

def move_down(x, y, board, path):

def find_manhattan_distance(x1, y1, x2, y2):
	return abs(x1 - x2) + abs(y1 - y2)

def get_manahattan_sum():
	manhattan_sum = 0
	for key in curr_positions:
		curr_x, curr_y = curr_positions[key][0], curr_positions[key][1]
		goal_x, goal_y = positions_of_goal[key][0], positions_of_goal[key][1]
		manhattan_sum += find_manhattan_distance(curr_x, curr_y, goal_x, goal_y)

	return manhattan_sum