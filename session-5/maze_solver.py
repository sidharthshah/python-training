import copy
import types
import random
from compiler.ast import flatten

ROWS = 3
COLS = 3
BLOCK_FILL_PERCENTAGE = float(0.20)

def generate_random_xy():
	return random.randint(0, ROWS-1), random.randint(0, COLS-1)

def is_valid_maze(maze):
	has_start = False
	has_end = False

	for row in maze:
		for cell in row:
			if cell == "1":
				has_start = True
				continue
			if cell == "2":
				has_end = True
	return has_start and has_end

def generate_maze():
	maze = []

	#Generate empty maze
	for i in range(ROWS):
		current_row = []
		for j in range(COLS):
			current_row.append("0")
		maze.append(current_row)	

	#Fill maze with blocks
	TOTAL_BLOCK_FILL = int(ROWS * COLS * BLOCK_FILL_PERCENTAGE)
	for i in range(TOTAL_BLOCK_FILL):
		x,y = generate_random_xy()
		maze[x][y] = "-1"

	#Put random start position
	start_x, start_y = generate_random_xy()
	maze[start_x][start_y] = "1"

	#Put random end position
	end_x, end_y = generate_random_xy()
	maze[end_x][end_y] = "2"

	if is_valid_maze(maze):
		return maze
	else:
		return None

def get_cords(maze, cell_value):
	for i in range(ROWS):
		for j in range(COLS):
			if maze[i][j] == cell_value:
				return i,j

def gen_child_state(maze):
	child_states = []
	current_x, current_y = get_cords(maze, "1")

	#Check if valid up action is possible
	new_x = current_x - 1
	new_y = current_y
	if new_x >=0 and maze[new_x][new_y] != "-1":
		current_child_state = copy.deepcopy(maze)
		current_child_state[new_x][new_y] = "1"
		current_child_state[current_x][current_y] = "0"
		child_states.append(current_child_state)

	#Check if valid right action is possible
	new_x = current_x
	new_y = current_y + 1
	if new_y <=COLS-1 and maze[new_x][new_y] != "-1":
		current_child_state = copy.deepcopy(maze)
		current_child_state[new_x][new_y] = "1"
		current_child_state[current_x][current_y] = "0"
		child_states.append(current_child_state)
	return child_states

#Print Maze
def print_maze(maze):
	if isinstance(maze, types.NoneType):
		return
	for row in maze:
		print "\t".join(row)

def print_solution_maze(solution):
	solution = solution.split(",")
	for i in range(ROWS):
		print "\t".join(solution[ROWS*i: (ROWS*i) + (COLS)])
	print "\n"
#Main
if __name__ == "__main__":
	#Generate a valid maze
	maze = generate_maze()
	while (isinstance(maze, types.NoneType)):
		maze = generate_maze()

	frontier = []
	solution = []
	visited = {}
	parent_state = {}
	found = False
	end_x, end_y = get_cords(maze, "2")
	print_maze(maze)
	frontier = gen_child_state(maze)

	parent_state[",".join(flatten(maze))] = None
	for initial_state in frontier:
		parent_state[",".join(flatten(initial_state))] = ",".join(flatten(maze))

	while(len(frontier) != 0):
		current_state = frontier.pop(0)
		current_x, current_y = get_cords(current_state, "1")
		
		#Check if current state needs to be terminated
		if (current_x == end_x and current_y == end_y):
			"Print found solution"
			found = True
			solution.append(",".join(flatten(current_state)))
			break

		#Skip if current state has already been visited
		if visited.has_key(",".join(flatten(current_state))):
			continue

		#Expand frontier & mark state as visited
		child_states = gen_child_state(current_state)
		if len(child_states) > 0 and not isinstance(child_states, types.NoneType):
			for new_state in child_states:
				frontier.append(new_state)
				parent_state[",".join(flatten(new_state))] = ",".join(flatten(current_state))
		visited[",".join(flatten(current_state))] = ""
		
	if not found:
		print "\n\nNo solution exists"
	else:
		print "\n\nSolution Found"
		while(not isinstance(parent_state[solution[-1]], types.NoneType)):
			solution.append(parent_state[solution[-1]])

		solution.reverse()
		for result in solution:
			print_solution_maze(result)
