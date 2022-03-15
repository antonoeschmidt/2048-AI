from board import Board
from copy import deepcopy

valid_actions = ['w', 'a', 's', 'd'] # WASD controls

def start_game():
    board = Board()
    board.add_new_num()
    board.print_state()
    while(True):
        action = input()
        if action == 'q':
            break

        """ Check if board is full"""
        if (is_terminal(board)):
            print("Game over")
            return
        
        if (action in valid_actions):
            """ If shuffle returns true, then it means that the board has changed and we can add a new number"""

            if (board.move(action, True)):
                board.add_new_num()            
            board.print_state()
            print(f'Score: {board.calculate_score()}')
            chance(board)
 
        else:
            print('Not a valid move')
       
    print('Finished')

def utility(state: Board):
    if (state.has_won()):
        return 1
    elif (len(actions(state) > 0)):
        return 0.5
    else:
        return 0

def actions(state: Board):
    possible_actions = []
    for action in valid_actions:
        if (state.move(action, False)):
            possible_actions.append(action)
    
    return possible_actions

def is_terminal(state: Board):
    return (len(actions(state)) < 1) or state.has_won()

def result(state: Board, action):
    state_copy = deepcopy(state)
    state_copy.move(action, True)
    return state_copy.board

def chance(state: Board):
    possible_boards = []
    probabilities = []
    for i in range(4):
        for j in range(4):
            if (state.board[i][j] == 0):
                for num in [2,4]:
                    state_copy = deepcopy(state)
                    state_copy.custom_add_new_num(i, j, num)
                    possible_boards.append(state_copy.board)
    
    for index in range(len(possible_boards)):
        if (index % 2 == 0):
            probabilities.append(0.9/(len(possible_boards)/2))
        else: 
            probabilities.append(0.1/(len(possible_boards)/2))
    
    return possible_boards, probabilities


                
start_game()