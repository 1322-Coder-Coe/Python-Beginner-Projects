# creating board spaces (3 rows of 3)
board_grid =[ 
    [1,2,3],
    [4,5,6],
    [7,8,9] 
    ]
 

#displaying board as 3x3 grid w/ update
def update():
 for row in board_grid:
    print(row)

update()
#creating space under grid
print()

#creating player input loop

while True:
    player_1 = int(input("Player 1: Which space would you like to mark with X? "))

# Mapping choice to grid locations
    if player_1 == 1:
      board_grid[0][0] = "X"
    elif player_1 == 2:
      board_grid[0][1] = "X"
    elif player_1 == 3:
      board_grid[0][2] = "X"
    elif player_1 == 4:
      board_grid[1][0] = "X"
    elif player_1 == 5:
      board_grid[1][1] = "X"
    elif player_1 == 6:
      board_grid[1][2] = "X"
    elif player_1 == 7:
      board_grid[2][0] = "X"
    elif player_1 == 8:
      board_grid[2][1] = "X"
    elif player_1 == 9:
      board_grid[2][2] = "X"

#creating space under display
    print()

# displaying user input mark in grid 
    update()
               
#creating space
    print()          
#player 2 input
    player_2 = int(input("Player 2: Which space would you like to mark with O? "))

# Mapping choice to grid locations
    if player_2 == 1:
      board_grid[0][0] = "O"
    elif player_2 == 2:
      board_grid[0][1] = "O"
    elif player_2 == 3:
      board_grid[0][2] = "O"
    elif player_2 == 4:
      board_grid[1][0] = "O"
    elif player_2 == 5:
      board_grid[1][1] = "O"
    elif player_2 == 6:
      board_grid[1][2] = "O"
    elif player_2 == 7:
      board_grid[2][0] = "O"
    elif player_2 == 8:
      board_grid[2][1] = "O"
    elif player_2 == 9:
      board_grid[2][2] = "O"

#creating space under display
    print()

# displaying user input mark in grid 
    update()