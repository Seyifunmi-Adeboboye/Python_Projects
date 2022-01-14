def win_game(current_game):
    
    for row in game:                                    # Horizontal Winner
        print(row)
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(f'Player {row[0]} wins the game horizontally') 
            return True
        
    for col in range(len(game)):                        # Vertical Winner
        check = []

        for row in game:
            check.append(row[col])

        if check.count(check[0]) == len(check) and check[0] != 0: 
            print(f'Player {check[0]} wins the game vertically')
            return True

    diags = []                                          # Diagonal Winner
      
    for i in range(len(game)):
        diags.append(game[i][i])

    if diags.count(diags[0]) == len(diags) and diags[0] != 0: 
            print(f'Player {diags[0]} wins the game diagonally!')
            return True

    cols = reversed(range(len(game)))
    rows = range(len(game))

    r_diags = []                                         # Diagonal Winner

    for cols, rows in zip(cols, rows):
        r_diags.append(game[rows][cols])

    if r_diags.count(r_diags[0]) == len(r_diags) and r_diags[0] != 0: 
            print(f'Player {r_diags[0]} wins the game diagonally!')
            return True
        
    return False
            
def tic_tac_toe(game_map, cur_player, row_choice, col_choice, just_display=False):
        try:
            if game_map[row_choice][col_choice] != 0:
                print('Choose another position: ')
                return game_map, False
            print('   0  1  2')
            if not just_display:
                game_map[row_choice][col_choice] = cur_player      
            for index, row in enumerate(game_map):
                print(index, row)
            return game_map, True
        
        except IndexError:
            print("Error: Wrong Input!, Row/Col_choice must be between 0 to 2")
            return game_map, False
        
import itertools

play = True
Players = [1, 2]

while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]
    
    game_won = False
    play_choice = itertools.cycle([1, 2])
    while not game_won:
        cur_player = next(play_choice) 
        print(f'Current Player: {cur_player}')
        played = False
        
        while not played:
            row_choice = int(input("Choose row between 0, 1, 2: "))
            col_choice = int(input("Choose column between 0, 1, 2: "))
            game, played = tic_tac_toe(game, cur_player, row_choice, col_choice)
        
        if win_game(game):
            game_won = True
            try_again = input('Try Again (yes/no): ')
            
            if try_again.lower() == 'yes':
                print('Start Again')
            
            elif try_again.lower() == 'no':
                print('Game End')
                play = False
                
            else:
                play = False
                
        