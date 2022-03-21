from ai.agent import Agent
from ai.program import Program
from board import Board
from ai.search.minimax import Minimax
from ai.search.minimax_ab import MinimaxAB
from ai.search.expectimax import Expectimax

minimax = Minimax(1)
minimax_ab = MinimaxAB(2)
expectimax = Expectimax(1)
algorithm = 0
choice = 0
gamemode = 0

print("Introduction to AI - Assignment 1")
print("Game: 2048")
print("Group 4")
print("")

while True:
    print("Input gamemode")
    print("1. Single player")
    print("2. AI")
    try:
        gamemode = int(input())
    except:
        print("Wrong input - pick a number")

    if gamemode == 1:
        break
    elif gamemode == 2:
        break
if gamemode == 2:
    while True:
        print("Pick algorithm")
        print("1. Minimax")
        print("2. Minimax - αß pruning")
        print("3. Expectimax - Best results")
        try:
            choice = int(input())
        except:
            print("Wrong input - pick a number")
        
        if choice == 1:
            algorithm = minimax
            break
        elif choice == 2:
            algorithm = minimax_ab
            break
        elif choice == 3:
            algorithm = expectimax
            break
else:
    algorithm = "human"
    print("Use WASD to move")

board = Board()
program = Program(board, algorithm)
agent = Agent(program)

agent.program.problem.start_game(agent)



