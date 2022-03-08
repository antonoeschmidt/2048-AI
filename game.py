from board import Board

valid_moves = ['w', 'a', 's', 'd'] # WASD controls

def start_game():
    board = Board()
    board.add_new_num()
    board.board[0][0] = 2
    board.board[1][0] = 2
    board.board[3][0] = 2
    board.print_state()
    while(True):
        x = input()
        if x == 'q':
            break

        """ Check if board is full"""
        if (board.is_full()):
            print("Game over")
            return
        
        if (x in valid_moves):
            board.shuffle(x)
            board.add_new_num()
            board.print_state()
        else:
            print('Not a valid move')
       
    
    print('Finished')

start_game()