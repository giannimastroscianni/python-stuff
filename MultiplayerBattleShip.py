dim = int(raw_input("Insert the number of rows and columns (at least 2): "))

player_one_matrix = [[0 for x in range(dim)] for x in range(dim)]
player_two_matrix = [[0 for x in range(dim)] for x in range(dim)]

def print_board(board):
  for row in board:
    line = ""
    for j in row:
      line += str(j) + " "
    print line

player_one = raw_input("Hi Player 1! Insert your name here ")
player_two = raw_input("Hi Player 2! Insert you name here ")
print ""
pippo = "Insert correct coordinates. Coordinates should be between 1 and %s. (Ex: 11 12) " % dim

error_one = 0
while error_one == 0:
  print "Hi %s. Insert the coordinates of your ship." % player_one
  ship_one = raw_input(pippo)

  player_one_ship_one_x = ship_one[0]
  player_one_ship_one_y = ship_one[1]
  player_one_ship_two_x = ship_one[3]
  player_one_ship_two_y = ship_one[4]

  if int(player_one_ship_one_x) == int(player_one_ship_two_x) and (
        int(player_one_ship_one_y) == (int(player_one_ship_two_y) + 1) or int(player_one_ship_one_y) == (
        int(player_one_ship_two_y) - 1)):
    error_one = 1
    print "Correct coordinates."  # spaces. they're necessary to hide the coordinates typed.
    print "Hide your coordinates!"
    print ""

  if int(player_one_ship_one_y) == int(player_one_ship_two_y) and (
        int(player_one_ship_one_x) == (int(player_one_ship_two_x) + 1) or int(player_one_ship_one_x) == (int(
      player_one_ship_two_x) - 1)):
    error_one = 1
    print "Correct coordinates."  # spaces. they're necessary to hide the coordinates typed.
    print "Hide your coordinates!"
    print ""

  if int(player_one_ship_one_x) == int(player_one_ship_two_x) & int(player_one_ship_one_y) == int(
    player_one_ship_two_y):
    print "Same coordinates. Try again"
    print ""

error_two = 0
while error_two == 0:
  print "Hi %s. Insert the coordinates of your ship." % player_two
  ship_two = raw_input(pippo)

  player_two_ship_one_x = ship_two[0]
  player_two_ship_one_y = ship_two[1]
  player_two_ship_two_x = ship_two[3]
  player_two_ship_two_y = ship_two[4]

  if int(player_two_ship_one_x) == int(player_two_ship_two_x) and (
        int(player_two_ship_one_y) == (int(player_two_ship_two_y) + 1) or int(player_two_ship_one_y) == (
        int(player_two_ship_two_y) - 1)):
    error_two = 1
    print "Correct coordinates."  # spaces. they're necessary to hide the coordinates typed.
    print "Hide your coordinates!"
    print ""

  if int(player_two_ship_one_y) == int(player_two_ship_two_y) and (
        int(player_two_ship_one_x) == (int(player_two_ship_two_x) + 1) or int(player_two_ship_one_x) == (int(
      player_two_ship_two_x) - 1)):
    error_two = 1
    print "Correct coordinates."  # spaces. they're necessary to hide the coordinates typed.
    print "Hide your coordinates!"
    print ""

  if int(player_two_ship_one_x) == int(player_two_ship_two_x) and int(player_two_ship_one_y) == int(
    player_two_ship_two_y):
    print "Same coordinates. Try again"
    print ""

player_one_matrix[int(player_one_ship_one_x) - 1][int(player_one_ship_one_y) - 1] = 1
player_one_matrix[int(player_one_ship_two_x) - 1][int(player_one_ship_two_y) - 1] = 1
player_two_matrix[int(player_two_ship_one_x) - 1][int(player_two_ship_one_y) - 1] = 1
player_two_matrix[int(player_two_ship_two_x) - 1][int(player_two_ship_two_y) - 1] = 1

# print_board(player_one_matrix)  # testing
print ""
# print_board(player_two_matrix)  # testing
print ""

# game loop
end = False
player_one_count = 0
player_two_count = 0

matrix_to_show_1 = [[0 for x in range(dim)] for x in range(dim)]
matrix_to_show_2 = [[0 for x in range(dim)] for x in range(dim)]

while end == False:
  print "%s's turn." % player_one
  print "Enemy's board:"
  print print_board(matrix_to_show_1)
  print "Where is the enemy ship?"
  reinsert = raw_input("Insert the coordinates. (Ex: 11) ")

  row = reinsert[0]
  column = reinsert[1]

  if player_two_matrix[int(row) - 1][int(column) - 1] == 1:
    player_one_count += 1
    player_two_matrix[int(row) - 1][int(column) - 1] = 0
    print "Good job! Part of the ship found!"
    matrix_to_show_1[int(row) - 1][int(column) - 1] = "Y"
    print ""
  else:
    print "Ship not hit! Try later!"
    matrix_to_show_1[int(row) - 1][int(column) - 1] = "N"
    print ""
  if player_one_count == 2:
    end = True
    print "Success! %s is the winner!" % player_one
    break

  print "%s's turn." % player_two
  print "Enemy's board:"
  print print_board(matrix_to_show_2)
  print "Where is the enemy ship?"
  reinsert = raw_input("Insert the coordinates. (Ex:11) ")

  row = reinsert[0]
  column = reinsert[1]

  if player_one_matrix[int(row) - 1][int(column) - 1] == 1:
    print "Good job! Part of the ship found!"
    player_two_count += 1
    player_one_matrix[int(row) - 1][int(column) - 1] = 0
    matrix_to_show_2[int(row) - 1][int(column) - 1] = "Y"
    print ""
  else:
    print "Ship not hit! Try later!"
    matrix_to_show_2[int(row) - 1][int(column) - 1] = "N"
    print ""
  if player_two_count == 2:
    end = True
    print "Success! %s is the winner!" % player_two
