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

#creating counter
turn_count = 0
#creating player input loop

while True:
    player_1 = int(input("Player 1: Which space would you like to mark with X? "))

# Mapping player_1 choice to grid locations
    
    if player_1 == 1:
        if board_grid[0][0] == "X" or board_grid[0][0] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
            board_grid[0][0] = "X"
            turn_count += 1
            
    elif player_1 == 2:
        if board_grid[0][1] == "X" or board_grid[0][1] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
            board_grid[0][1] = "X"
            turn_count += 1
            
    elif player_1 == 3:
        if board_grid[0][2] == "X" or board_grid[0][2] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
            board_grid[0][2] = "X"
            turn_count += 1
            
    elif player_1 == 4:
        if board_grid[1][0] == "X" or board_grid[1][0] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
            board_grid[1][0] = "X"
            turn_count += 1
            
    elif player_1 == 5:
        if board_grid[1][1] == "X" or board_grid[1][1] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
            board_grid[1][1] = "X"
            turn_count += 1
            
    elif player_1 == 6:
        if board_grid[1][2] == "X" or board_grid[1][2] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
            board_grid[1][2] = "X"
            turn_count += 1
            
    elif player_1 == 7:
        if board_grid[2][0] == "X" or board_grid[2][0] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
             board_grid[2][0] = "X"
             turn_count += 1
             
    elif player_1 == 8:
        if board_grid[2][1] == "X" or board_grid[2][1] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
             board_grid[2][1] = "X"
             turn_count += 1
             
    elif player_1 == 9:
        if board_grid[2][2] == "X" or board_grid[2][2] == "O": 
            print("Spot is taken! Pick another spot: ")
            print()
            continue
        else: 
             board_grid[2][2] = "X"
             turn_count += 1
#creating space under display
    print()

# displaying user input mark in grid 
    update()
    #applying test for win in first loop
        # Check all Player 1 win conditions
    if (
        (board_grid[0][0] == "X" and board_grid[0][1] == "X" and board_grid[0][2] == "X") or # Top row
        (board_grid[1][0] == "X" and board_grid[1][1] == "X" and board_grid[1][2] == "X") or # Middle row
        (board_grid[2][0] == "X" and board_grid[2][1] == "X" and board_grid[2][2] == "X") or # Bottom row
        (board_grid[0][0] == "X" and board_grid[1][0] == "X" and board_grid[2][0] == "X") or # Left column
        (board_grid[0][1] == "X" and board_grid[1][1] == "X" and board_grid[2][1] == "X") or # Middle column
        (board_grid[0][2] == "X" and board_grid[1][2] == "X" and board_grid[2][2] == "X") or # Right column
        (board_grid[0][0] == "X" and board_grid[1][1] == "X" and board_grid[2][2] == "X") or # Diagonal top-left to bottom-right
        (board_grid[0][2] == "X" and board_grid[1][1] == "X" and board_grid[2][0] == "X")    # Diagonal top-right to bottom-left
    ):
        print("Congratulations Player 1! You Won")
        break

    # Check all Player 2 win conditions
    elif (
        (board_grid[0][0] == "O" and board_grid[0][1] == "O" and board_grid[0][2] == "O") or 
        (board_grid[1][0] == "O" and board_grid[1][1] == "O" and board_grid[1][2] == "O") or 
        (board_grid[2][0] == "O" and board_grid[2][1] == "O" and board_grid[2][2] == "O") or 
        (board_grid[0][0] == "O" and board_grid[1][0] == "O" and board_grid[2][0] == "O") or 
        (board_grid[0][1] == "O" and board_grid[1][1] == "O" and board_grid[2][1] == "O") or 
        (board_grid[0][2] == "O" and board_grid[1][2] == "O" and board_grid[2][2] == "O") or 
        (board_grid[0][0] == "O" and board_grid[1][1] == "O" and board_grid[2][2] == "O") or 
        (board_grid[0][2] == "O" and board_grid[1][1] == "O" and board_grid[2][0] == "O")
    ):
        print("Congratulations Player 2! You Won")
        break
        
    elif turn_count == 9:
        print("It's a Draw!")
        break

#creating space
    print()          
    
    # creating nested while loop for player 2
    while True:
        player_2 = int(input("Player 2: Which space would you like to mark with O? "))
        
        # Mapping player_2 choice to grid locations
        if player_2 == 1:
            if board_grid[0][0] == "X" or board_grid[0][0] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[0][0] = "O"            
                turn_count += 1
                break
                
        elif player_2 == 2:
            if board_grid[0][1] == "X" or board_grid[0][1] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[0][1] = "O"
                turn_count += 1
                break
                
        elif player_2 == 3:
            if board_grid[0][2] == "X" or board_grid[0][2] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[0][2] = "O"
                turn_count += 1
                break
                
        elif player_2 == 4:
            if board_grid[1][0] == "X" or board_grid[1][0] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[1][0] = "O"
                turn_count += 1
                break
                
        elif player_2 == 5:
            if board_grid[1][1] == "X" or board_grid[1][1] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[1][1] = "O"
                turn_count += 1
                break
                
        elif player_2 == 6:
            if board_grid[1][2] == "X" or board_grid[1][2] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[1][2] = "O"
                turn_count += 1
                break
                
        elif player_2 == 7:
            if board_grid[2][0] == "X" or board_grid[2][0] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[2][0] = "O"
                turn_count += 1
                break
                
        elif player_2 == 8:
            if board_grid[2][1] == "X" or board_grid[2][1] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[2][1] = "O"
                turn_count += 1
                break
                
        elif player_2 == 9:
            if board_grid[2][2] == "X" or board_grid[2][2] == "O": 
                print("Spot is taken! Pick another spot: ")
                print()
                continue
            else: 
                board_grid[2][2] = "O"
                turn_count += 1
                break

    # creating space under display
    print()

    # displaying user input mark in grid 
    update()
    print()

      
 # Check all Player 1 win conditions
    if (
        (board_grid[0][0] == "X" and board_grid[0][1] == "X" and board_grid[0][2] == "X") or # Top row
        (board_grid[1][0] == "X" and board_grid[1][1] == "X" and board_grid[1][2] == "X") or # Middle row
        (board_grid[2][0] == "X" and board_grid[2][1] == "X" and board_grid[2][2] == "X") or # Bottom row
        (board_grid[0][0] == "X" and board_grid[1][0] == "X" and board_grid[2][0] == "X") or # Left column
        (board_grid[0][1] == "X" and board_grid[1][1] == "X" and board_grid[2][1] == "X") or # Middle column
        (board_grid[0][2] == "X" and board_grid[1][2] == "X" and board_grid[2][2] == "X") or # Right column
        (board_grid[0][0] == "X" and board_grid[1][1] == "X" and board_grid[2][2] == "X") or # Diagonal top-left to bottom-right
        (board_grid[0][2] == "X" and board_grid[1][1] == "X" and board_grid[2][0] == "X")    # Diagonal top-right to bottom-left
    ):
        print("Congratulations Player 1! You Won")
        break

    # Check all Player 2 win conditions
    elif (
        (board_grid[0][0] == "O" and board_grid[0][1] == "O" and board_grid[0][2] == "O") or 
        (board_grid[1][0] == "O" and board_grid[1][1] == "O" and board_grid[1][2] == "O") or 
        (board_grid[2][0] == "O" and board_grid[2][1] == "O" and board_grid[2][2] == "O") or 
        (board_grid[0][0] == "O" and board_grid[1][0] == "O" and board_grid[2][0] == "O") or 
        (board_grid[0][1] == "O" and board_grid[1][1] == "O" and board_grid[2][1] == "O") or 
        (board_grid[0][2] == "O" and board_grid[1][2] == "O" and board_grid[2][2] == "O") or 
        (board_grid[0][0] == "O" and board_grid[1][1] == "O" and board_grid[2][2] == "O") or 
        (board_grid[0][2] == "O" and board_grid[1][1] == "O" and board_grid[2][0] == "O")
    ):
        print("Congratulations Player 2! You Won")
        break
        
    elif turn_count == 9:
        print("It's a Draw!")
        break