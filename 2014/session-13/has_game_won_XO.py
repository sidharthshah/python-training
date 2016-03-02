def has_game_won_XO(x):
	for i in range(3):
		if x[0][i] == x[1][i] == x[2][i]:
			return True

		if x[i][0] == x[i][1] == x[i][2]:
			return True

	if x[0][0] == x[1][1] == x[2][2] or x[0][2] == x[1][1] == x[2][0]:
		return True

	return False

if __name__ == "__main__":
	print has_game_won_XO([
		['x','o','x'],
		['x','o','o'],
		['o','x','x']])