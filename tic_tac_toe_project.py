# creating board spaces (3 rows of 3)
board_grid =[ 
    [1,2,3],
    [4,5,6],
    [7,8,9] 
    ]
 

#displaying board as 3x3 grid
def update():
 for row in board_grid:
    print(row)

update()
print()

#creating user input logic
choice = int(input("which space would you like to mark? "))

# Mapping choice to grid locations
if choice == 1:
    board_grid[0][0] = "X"
elif choice == 2:
    board_grid[0][1] = "X"
elif choice == 3:
    board_grid[0][2] = "X"
elif choice == 4:
    board_grid[1][0] = "X"
elif choice == 5:
    board_grid[1][1] = "X"
elif choice == 6:
    board_grid[1][2] = "X"
elif choice == 7:
    board_grid[2][0] = "X"
elif choice == 8:
    board_grid[2][1] = "X"
elif choice == 9:
    board_grid[2][2] = "X"
    
update()
                
               
